n = int(input())
a = [int(i) for i in input().split()]

b = [0]*10**5

for i in a:
    b[i] += 1
ans = 0
c = 0
for i in range(10**5):
    if b[i] == 0:
        continue
    if b[i] == 1:
        ans +=1
    elif b[i] % 2 == 0:
        c += 1
    elif b[i] % 2 == 1:
        ans +=1
        
d = c % 2
if d == 1:
    ans -=1
print(ans + c)