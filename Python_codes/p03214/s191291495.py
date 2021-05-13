N = int(input())
a = list(map(int,input().split()))
ave = sum(a)/N
min = idx = 10**9
for i in range(N):
    if abs(ave-a[i])<min:
        min = abs(ave-a[i])
        idx = i
print(idx)
