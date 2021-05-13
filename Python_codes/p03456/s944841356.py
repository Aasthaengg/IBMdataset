a = int(input().replace(" ",""))
c=0
for i in range(10**4):
    if i**2 <= a:c=i**2
    else:break
print("Yes" if c == a else "No")