n = int(input())
s1 = list(input())
s2 = list(input())
mod = int(1e9+7)

def ranl(lst):
    ans = []
    cnt = 1
    ini = lst[0]
    for i in range(1, len(lst)):
        if ini == lst[i]:
            cnt += 1
        else:
            ans.append((ini, cnt))
            cnt = 1
            ini = lst[i]
    ans.append((ini, cnt))
    return ans

lst = ranl(s1)
ans = 1
if lst[0][1] == 1:
    ans *= 3
else:
    ans *= 6

for i in range(1, len(lst)):
    if lst[i-1][1] == 1 and lst[i][1] == 1:
        ans *= 2
        ans %= mod
    elif lst[i-1][1] == 1 and lst[i][1] == 2:
        ans *= 2
        ans %= mod
    elif lst[i-1][1] == 2 and lst[i][1] == 1:
        ans *= 1
    else:
        ans *= 3
        ans %= mod
print(ans)



