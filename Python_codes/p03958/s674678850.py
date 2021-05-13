K,T = list(map(int,input().split()))
A = list(map(int,input().split()))
MA = max(A)
out = 0
if MA > K-MA+1:
    out += MA-(K-MA+1)
print(out)
