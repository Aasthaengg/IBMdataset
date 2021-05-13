n = int(input())
d = list(map(int, input().split()))
d_s = sorted(d)
k = d_s[n//2] - d_s[n//2-1]
print(k)