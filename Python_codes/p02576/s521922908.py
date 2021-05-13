import math

N, X, T = map(int,input().split())

count = math.ceil(N/X);

ans = count*T

print(ans)
