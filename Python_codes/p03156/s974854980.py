import math
import statistics
a=int(input())
# b=input()
# c=[]
# for i in b:
#     c.append(i)
e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(3)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
a1=[]
b1=[]
c1=[]
for i in range(a):
    if f[i]<=e1:
        a1.append(f[i])
    if e1<f[i]<=e2:
        b1.append(f[i])
    if e2<f[i]:
        c1.append(f[i])

lis = [len(a1),len(b1),len(c1)]
print(min(lis))