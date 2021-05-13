N,K = map(int,input().split())
S = input()
cnt01 = []
for i,s in enumerate(S):
    if i == 0:
        if s == "0":
            cnt01.append([1,0])
        cnt01.append([s,1])
    else:
        if cnt01[-1][0] == s:
            cnt01[-1][1] += 1
        else:
            cnt01.append([s,1])
if len(cnt01) <= 2*K+1:
    ans = sum([cnt[1] for cnt in cnt01])
    print(ans)
    exit()
else:
    ans = [sum([cnt[1] for cnt in cnt01[0:2*K+1]])]
    pos = 2
    while True:
        temp = ans[-1] - cnt01[pos-2][1] - cnt01[pos-1][1]
        if len(cnt01)-1 >= (pos + 2*K -1):
            temp += cnt01[pos+2*K-1][1]
        else:
            break
        if len(cnt01)-1 >= (pos + 2*K):
            temp += cnt01[pos+2*K][1]
        else:
            ans.append(temp)
            break
        ans.append(temp)
        pos += 2
print(max(ans))
