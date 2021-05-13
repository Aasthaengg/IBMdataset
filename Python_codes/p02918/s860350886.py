n,k = map(int,input().split())
s = list(input())
def ranl(lst):
    ans = []
    cnt = 1
    ini = lst[0]
    for i in range(1, len(lst)):
        if ini == lst[i]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            ini = lst[i]
    ans.append(cnt)
    return ans
s = ranl(s)
if len(s)//2 <= k:
    print(n-1)
else:
    cnt = 0
    cnt += sum(s[0:2*k+1]) - 1
    for i in range(2*k+1, len(s)):
        cnt += s[i]-1
    print(cnt)

