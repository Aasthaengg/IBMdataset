import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
m = 10**9+7
sumA = 0
for i in range(60):
    cnt1 = 0
    for a in A:
        if a>>i & 1:
            cnt1 += 1
    sumA += (cnt1*(N-cnt1)*2**i)%m
print(sumA%m)
