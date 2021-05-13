n = int(input())
ls = list(map(str,input().split()))
lso = ls[::2]
lse = ls[1::2]
if n % 2 == 0:
    ans = lse[::-1] + lso
else:
    ans = lso[::-1] + lse
p =" ".join(ans)
print(p)
