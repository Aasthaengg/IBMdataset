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

s1 = str(input())
s2 =str(input())
d1, d2 = 0,0
for i in range(len(s1)):
    if(s1[i] != s2[i]):
        d1+=1
print(d1)
