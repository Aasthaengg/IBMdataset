import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(ans)
    return ans


n, k = map(int, input().split())
s = set()
for i in range(k):
    d=int(input())
    ls = list(map(int, input().split()))
    for i in range(d):
        s.add(ls[i])
print(n-len(s))