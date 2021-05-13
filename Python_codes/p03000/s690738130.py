# coding: utf-8
# Your code here!
N,X=map(int, input().split())
List=list(map(int, input().split()))
bow=0
cnt=1
for i in range(0,N):
    bow+=List[i]
    if bow>X:
        break
    else:
        cnt+=1

print(cnt)