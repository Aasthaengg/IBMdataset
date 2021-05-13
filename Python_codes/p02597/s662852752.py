import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

n=int(input())
c=list(input().rstrip("\n"))
import collections
cc=collections.Counter(c)
ans=0
for i in range(cc["R"]):
    if c[i]=="W":
        ans+=1
print(ans)