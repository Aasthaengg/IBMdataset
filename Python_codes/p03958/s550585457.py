K, T = map(int, input().split())
a = list(map(int, input().split()))
s, t = max(a)<<1, sum(a)
if s > t:
    print(s-t-1)
else:
    print(0)