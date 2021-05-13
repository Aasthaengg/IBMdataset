A,B,C,K = map(int, input().split())
#4 0 2   3
#3 2 4   5
#1 0 -1
ans = 0

if A < K:
    K -= A
    ans += A
else:
    ans = K
    K = 0

K -= B

if K > 0:
    ans -= K

print(ans)