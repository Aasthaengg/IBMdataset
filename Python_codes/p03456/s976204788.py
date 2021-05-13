a,b=input().split()
num = int(a+b)

ans = "No"

for i in range(320):
    if i**2 != num:
        continue
    else:
        ans = "Yes"
        break
print(ans)