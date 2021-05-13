from decimal import Decimal as d
a,b,c = map(int,input().split())
if d(a)**d(0.5) + d(b)**d(0.5) < d(c)**d(0.5):
    ans = "Yes"
else:
    ans = "No"
print(ans)