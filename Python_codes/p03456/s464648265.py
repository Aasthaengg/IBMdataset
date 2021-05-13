a, b = map(str, input().split())
res = int(a+b)
ans = "No"
for i in range(int(res**0.5)+1):
    if i**2 == res:
        ans = "Yes"
        break
print(ans)
