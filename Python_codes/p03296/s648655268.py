# import math
# import statistics
# import itertools
a=int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
# N,S,T= map(int,input().split())
f = list(map(int,input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
count=1
ans=0
for i in range(a-1):
    if f[i]==f[i+1]:
        count+=1
    elif f[i]!=f[i+1]:
        count=1
    if count==2 :
        ans+=1
        count=0

print(ans)
