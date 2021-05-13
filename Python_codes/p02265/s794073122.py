from collections import deque

class MyList(deque):
    def __init__(self):
        self.__init__ = deque
        self.d = {'deleteFirst':self.delF, 'deleteLast':self.delL, 'insert':self.insX, 'delete':self.delX}
    def cmd(self,command):
        if ' ' in command:
            ope, num = command.split()
            num = int(num)
            self.d[ope](num)
        else:
            self.d[command]()
            
    def delF(self):
        self.popleft()

    def delL(self):
        self.pop()

    def insX(self,num):
        self.appendleft(num)

    def delX(self,num):
        if num in self:
            self.remove(num)

if __name__ == '__main__' :
    l = MyList()
    n = input()
    
    for i in range(n):
        l.cmd(raw_input())

    q = deque(l)
    for i in range(len(l)-1):
        print q.popleft(),
    print l[-1]