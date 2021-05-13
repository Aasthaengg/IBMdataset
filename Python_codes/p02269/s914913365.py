class Dictionary:
    def __init__(self):
        self.data = {}
        
    def insert(self, value:str):
        self.data[value] = True

    def find(self, value:str):
        if value in self.data:
            return 'yes'
        return 'no'

if __name__ == '__main__':
    my_dict = Dictionary()
    n = int(input())
    for _ in range(n):
        comm = list(map(str, input().rstrip().split()))
        if comm[0] == 'insert':
            my_dict.insert(comm[1])
        elif comm[0] == 'find':
            print(my_dict.find(comm[1]))
