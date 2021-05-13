import sys

class HashTable:
    def __init__(self):
        self.table = [None] * 4
        self.flag = False

class Dictionary:
    def __init__(self):
        self.hashTable = HashTable()

    def insert(self, key):
        table = self.hashTable
        for c in key:
            hash = self.toHash(c)
            if table.table[hash] is None:
                table.table[hash] = HashTable()
            table = table.table[hash]
        table.flag = True

    def find(self, key):
        table = self.hashTable
        for c in key:
            hash = self.toHash(c)
            if table.table[hash] is None:
                return False
            table = table.table[hash]
        if table.flag:
            return True
        else:
            return False

    def toHash(self, key):
        if key == "A":
            return 0
        elif key == "C":
            return 1
        elif key == "G":
            return 2
        else:
            return 3

if __name__ == "__main__":
    dic = Dictionary()
    lines = sys.stdin.readlines()
    del lines[0]
    for command in lines:
        key = command.split()[1]
        if command[0] == "i":
            dic.insert(key)
        else:
            if dic.find(key):
                print "yes"
            else:
                print "no"