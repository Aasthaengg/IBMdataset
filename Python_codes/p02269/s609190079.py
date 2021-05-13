class diction:
    def __init__(self):
        self.D = {}
    def insert(self,string):
        self.D[string] = True
    def find(self,string):
        try:
            if self.D[string]:print('yes')
        except KeyError:
            print('no')
            
D = diction()
for _ in range(int(input())):
    command,string = input().split()
    if command == 'insert':
        D.insert(string)
    elif command == 'find':
        D.find(string)
