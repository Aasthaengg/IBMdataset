n=int(input())
a=list(map(int,input().split()))
ushiro=list()
mae=list()
for i in range(n):
    if i%2:#1
        mae.append(a[i])
    else:
        ushiro.append(a[i])
p=ushiro[::-1]+mae if n%2 else mae[::-1]+ushiro
print(*p)