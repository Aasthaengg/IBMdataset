k, s = map(int,input().split())
 
ans = 0
for i in range(k+1):
    yz = s - i
    for j in range(k+1):
        if k >= yz - j >= 0:
            ans += 1

print(ans)