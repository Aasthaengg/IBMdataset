import sys
input = sys.stdin.readline

N=int(input())
a = tuple(map(int,input().split()))
sum = 0

for i in range(N):
    if a[i] > i+1:
        if a[a[i]-1] == i+1:
            sum += 1

print(sum)