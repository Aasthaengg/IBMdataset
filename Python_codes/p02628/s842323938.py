import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(list(dict.fromkeys(ans)))
    if(ans[-1]==n):
        ans = ans[:-1]
    return ans

n,k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = sum(nums[:k])
print(ans)
