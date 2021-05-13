import sys
def I(): return int(sys.stdin.readline().rstrip())
N = I()
s = sorted([I() for _ in range(N)])
ans = sum(s)
if ans%10==0:
    for x in s:
        if x%10!=0:
            ans -= x
            break
    else:
        ans = 0
print(ans)
