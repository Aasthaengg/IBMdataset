# coding: utf-8

n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))

p.sort()

cnt = [0,0,0]

for i in range(0,n):
    if(p[i] <= a):
        cnt[0]+=1
    elif(a < p[i] <= b):
        cnt[1]+=1
    else:
        cnt[2]+=1

#print(cnt)
print(min(cnt))