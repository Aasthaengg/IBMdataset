N = int(input())
K = int(input())
X = int(input())
Y = int(input())
ans = 0
if N>=K:
    ans = K*X+(N-K)*Y
if N<K:
    ans = N*X
print(ans)