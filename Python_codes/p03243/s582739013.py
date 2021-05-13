n = int(input())
ans = 999
for i in range(1,10):
    if 111*i-n>=0:
        ans = min(ans,111*i-n)
print(ans+n)