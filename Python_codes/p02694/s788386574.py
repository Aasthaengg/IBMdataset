import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(ans)
    return ans


x = int(input())
ans = 1
cnt = 101
while(cnt < x):
    ans+=1
    cnt+=(cnt//100)
print(ans)
