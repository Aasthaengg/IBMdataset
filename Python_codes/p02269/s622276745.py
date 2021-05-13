class HashTable:

    @staticmethod
    def h1(key):
        return key % 1046527

    @staticmethod
    def h2(key):
        return 1 + (key % (1046527 - 1))
    
    def __init__(self, size):
        self.size = size
        self.values = [None for _ in range(size)]
        self.tables = str.maketrans({
            'A':'1', 'C':'2', 'G':'3', 'T':'4',
        })

    def translate_key(self, value):
        return int(value.translate(self.tables))

    def find(self, value):
        count = 0
        key = self.translate_key(value)

        while True:
            h = (HashTable.h1(key) + count * HashTable.h2(key)) % 1046527
            if self.values[h] == value:
                return True
            elif self.values[h] is None:
                return False
            count += 1
        return False

    def insert(self, value):
        count = 0
        key = self.translate_key(value)
        
        while True:
            h = (HashTable.h1(key) + count * HashTable.h2(key)) % 1046527
            if self.values[h] is None:
                self.values[h] = value
                break
            count += 1


num = int(input())

dictionary = HashTable(1046527)
for _ in range(num):
    command, value = input().split()
    if command == "insert":
        dictionary.insert(value)
    elif command == "find":
        is_find = dictionary.find(value)
        print("yes" if is_find else "no")
