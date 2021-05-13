def wa(int_n):
    str_n = str(int_n)
    ans = 0
    for i in range(len(str_n)):
        ans += int(str_n[i])
    return ans
    
n,a,b = map(int,input().split())
ans = 0
for i in range(n+1):
    if a<=wa(i)<=b:
        ans += i
print(ans)
