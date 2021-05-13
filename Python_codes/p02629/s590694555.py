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

n = int(input())
ans = ''
for i in range(1, 99):
    if(n <= 26**i):
        n-=1
        for i in range(i):
            ans+=(chr(ord('a')+n%26))
            n//=26
        break
    else:
        n-=26**i
ans = ans[::-1]
print(ans)