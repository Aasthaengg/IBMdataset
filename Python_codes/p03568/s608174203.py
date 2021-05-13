import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

ans = 3 ** n
mi = 1
for i in range(n):
    if A[i] % 2 == 0:
        mi *= 2
print(ans - mi)