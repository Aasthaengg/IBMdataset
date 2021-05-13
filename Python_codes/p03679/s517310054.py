#ABC065 A - Expired
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
x,a,b = nm()
e = -a+b
ans = ''
if e<=0:
    ans = 'delicious'
elif e<=x:
    ans = 'safe'
else:
    ans = 'dangerous'

print(ans)
