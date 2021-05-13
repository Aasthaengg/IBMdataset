K = int(input())

ans = -1
mod = 7%K
for i in range(1000001):
    if mod==0:
        ans = i+1
        break
    else:
        mod = (mod*10+7)%K
        
print(ans)