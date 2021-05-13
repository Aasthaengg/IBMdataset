from itertools import combinations
N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
arr=[0]*3

for i in range(N):
    if P[i]<=A:
        arr[0]+=1
    elif P[i]<=B:
        arr[1]+=1
    else:
        arr[2]+=1
print(min(arr))