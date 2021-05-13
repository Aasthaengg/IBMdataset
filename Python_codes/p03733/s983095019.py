n, t = map(int, input().split())
T = list(map(int, input().split()))
r = t
for i in range(n-1):
    r += min(T[i+1]-T[i], t)
print(r)