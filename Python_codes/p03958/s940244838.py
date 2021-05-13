k,t = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

print(max(0, a[-1] - sum(a[:-1]) - 1))
