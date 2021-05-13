import sys
input = sys.stdin.readline
 
K,S=map(int,input().split())
count=0
for x in range(K+1):
    for y in range(K+1):
        if S-(x+y)>=0 and S-(x+y)<=K: count+=1
print(count)