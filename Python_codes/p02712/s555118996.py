num = int(input())

ls = []

for i in range(num):
    ls.append(True)

f = 3
z = 5

while f <= num:
    ls[f-1] = False
    f += 3

while z <= num :
    ls[z-1] = False
    z += 5

ans = 0

for i in range(num):
    if ls[i]:
        ans += i+1
    
print(ans)