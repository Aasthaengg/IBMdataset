import sys
a,b,c = map(int,input().split())
if a >= c or b >= c:
    print("No")
    sys.exit()
if a**2+b**2+c**2-2*a*b-2*a*c-2*b*c > 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)