def digit_sum(x):
    ans=0
    while x>0:
        ans+=x%10
        x=int(x/10)

    return ans

n = int(input())
ans = 100
for a in range(1,int(n/2)+1):
    ans = min(ans, digit_sum(a)+digit_sum(n-a))

print(ans)
