from sys import stdin
import math
# from sympy import nextprime
class hash():
    def __init__(self,n):#ｎは素数
        self.n=1000003
        self.memo=[None]*self.n
    def madekey(self,key):
        if key=='A':return '1'
        elif key=='C':return '2'
        elif key=='G':return '3'
        elif key=='T':return '4'
    def getkey(self,KEY):
        key=""
        for S in KEY:
            key=key+self.madekey(S)
        return int(key)
    def h1(self,key):
        return key%self.n
    def h2(self,key):
        return (key%(self.n-1))+1
    def insert(self,S):
        key=self.getkey(S)
        h1 = self.h1(key)
        h2 = self.h2(key)
        for i in range(0,self.n+1):
            j=(h1+(i*h2)) % self.n
            if self.memo[j] is None:
                self.memo[j]=S
                break

    def search(self,S):
        key = self.getkey(S)
        h1 = self.h1(key)
        h2 = self.h2(key)
        for i in range(0,self.n+1):
            j = (h1+(i*h2)) % self.n
            if self.memo[j] ==S:
                return 'yes'
            elif self.memo[j] is None or i ==self.n:
                return 'no'
n=list(map(int,(stdin.readline().strip().split())))
dic=hash(n)
for _ in range(n[0]):
    S =list(stdin.readline().strip().split())
    if S[0]=='insert':
        dic.insert(S[1])
    elif S[0]=='find':
        print(dic.search(S[1]))

