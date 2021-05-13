import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += bin(A[i])[::-1].find('1')
print(ans)
