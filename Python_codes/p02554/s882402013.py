N = int(input())
M = 10**9+7
A = 8**N
B = 9**N
C = 10**N
ans = (C - B*2 + A)%M
print(ans)
