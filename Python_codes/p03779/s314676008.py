X = int(input())

ans=0
l_befor=0
for n in range(10**7):
    l_befor = n+l_befor
    if l_befor >= X:
        ans=n
        break
print(ans)