import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
odd = 0

for Ai in A:
    if Ai%2==1:
        odd += 1

if odd%2==0:
    print('YES')
else:
    print('NO')