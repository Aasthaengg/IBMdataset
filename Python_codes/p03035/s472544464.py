age,price = map(int,input().split())

if age >= 13:
    ans = price
elif age >= 6:
    ans = price//2
else:
    ans = 0

print(ans)