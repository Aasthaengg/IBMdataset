a,b,c,d = map(int, input().split())
while(a > 0 and c > 0) :
    c -= b
    a -= d
if(c <= 0) :
    ans = "Yes"
else :
    ans = "No"
print(ans)