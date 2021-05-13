n = int(input())
v = list(map(int,input().split()))
v1 = sorted(v[0::2])
v2 = sorted(v[1::2])
s1 = set(v1)
s2 = set(v2)

eve = [[0,0]]
odd = [[0,0]]
cnt_eve = 1
cnt_odd = 1

for i in range(1,n//2):
    ## 偶数項
    if v1[i] == v1[i-1]:
        cnt_eve += 1
    else:
        eve.append([cnt_eve, v1[i-1]])
        cnt_eve = 1
    ## 奇数項
    if v2[i] == v2[i-1]:
        cnt_odd += 1
    else:
        odd.append([cnt_odd, v2[i-1]])
        cnt_odd = 1
    if i == n//2 - 1:
        eve.append([cnt_eve, v1[i]])
        odd.append([cnt_odd, v2[i]])


eve.sort(key=lambda x: x[0], reverse=True)
odd.sort(key=lambda x: x[0], reverse=True)

if eve[0][1] != odd[0][1]:
    ans = n - eve[0][0] - odd[0][0]
    print(ans)
else:
    ans = n - max(eve[0][0] + odd[1][0], eve[1][0] + odd[0][0])
    print(ans)