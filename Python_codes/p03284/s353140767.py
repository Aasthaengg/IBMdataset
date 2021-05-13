n, k = map(int, input().split())
N = n//k
m = n%k
print(0 if m==0 else 1)