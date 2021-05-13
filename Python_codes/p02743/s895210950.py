from decimal import Decimal as d
a,b,c = map(int,input().split())
if a**d(0.5) + b**d(0.5) < c**d(0.5):
    ans = "Yes"
else:
    ans = "No"
print(ans)