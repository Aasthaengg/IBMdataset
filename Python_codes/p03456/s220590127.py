#8
a,b = map(str,input().split())
c = int(a+b)
Ans = "No"

for i in range(1,1001):
    if i**2 == c:
        Ans = "Yes"

print(Ans)
