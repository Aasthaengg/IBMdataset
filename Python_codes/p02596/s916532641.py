K = int(input())
 
num = 0
cnt = 0
ans = -1
 
for i in range(K):
    num = num*10 +7
    cnt += 1
    if num%K != 0:
        num = num%K
    else:
        ans = cnt
        break
    
print(ans)