n,m = map(int,input().split())
S = input()
ans = []
cur = n
temp = 0
flag = True
while cur != 0:
    kouho = 0
    for i in range(1,m+1):
        if cur-i >= 0:
            if S[cur-i] == '0':
                kouho = max(kouho, i)
    if kouho == 0:
        flag = False
        break
    else:
        ans.append(kouho)
        cur = cur-kouho
if flag:
    ans.reverse()
    print(' '.join(map(str, ans)))
else:
    print(-1)
