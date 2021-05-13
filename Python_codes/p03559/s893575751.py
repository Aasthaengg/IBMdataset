import bisect
def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))

n = II()
a, b, c = sorted(LI()), LI(), sorted(LI())
ans = 0
for _b in b:
    a_index = bisect.bisect_left(a,_b)
    c_index = bisect.bisect_right(c,_b)
    ans += a_index * (n - c_index)
print(ans)

    

