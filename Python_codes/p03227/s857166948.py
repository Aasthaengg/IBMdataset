# import math
# import statistics
a=input()
#b,c=int(input()),int(input())
c=[]
for i in a:
    c.append(i)
#e1,e2 = map(int,input().split())
#f = list(map(int,input().split()))
#g = [input() for _ in range(a)]

if len(c)==2:
    print(a)
elif len(c)==3:
    c.reverse()
    print("".join(c))