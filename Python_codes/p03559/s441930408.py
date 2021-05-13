import bisect
f = lambda: map(int,input().split())
n = int(input())
a = sorted(list(f()))
b = sorted(list(f()))
c = sorted(list(f()))

ans = 0
for i in b:
    ans += bisect.bisect_left(a,i)*(n-bisect.bisect(c,i))
print(ans)