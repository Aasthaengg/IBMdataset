n = int(input())
al = list(map(int, input().split()))
res = 0
temp = 0
for j in range(n-1,-1,-1):
    if j ==al[j]-1:
        temp +=1
    else:
        break
if temp % 2 ==1:
    res +=1

for i in range(n-1):
    if al[i] ==i+1:
        res += 1
        al[i+1] = al[i]

print(res)