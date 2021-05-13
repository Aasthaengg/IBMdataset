n = int(input())
plus = []
minus = []
for a in map(int,input().split()):
    if a>=0:
        plus.append(a)
    else:
        minus.append(a)
ans = sum(plus)-sum(minus)
if len(minus)%2==1:
    if plus==[]:
        ans = ans + 2*max(minus)
    else:
        ans = ans - 2*min(abs(max(minus)),min(plus))
print(ans)