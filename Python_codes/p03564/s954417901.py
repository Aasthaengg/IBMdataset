n = int(input())
k = int(input())
cnt = 0
ans = 1

while n > cnt:
    ans = min(ans*2, ans+k)
    cnt += 1
    
print(ans)