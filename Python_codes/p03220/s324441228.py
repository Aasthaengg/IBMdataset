n=int(input())
t,a = map(int, input().split())
H = list(map(int, input().split()))

min_abs = float("inf")

for i in range(n):
    if abs((t-H[i]*0.006)-a)< min_abs:
        min_abs = abs((t-H[i]*0.006)-a)
        ans = i+1
print(ans)