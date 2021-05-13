n,c = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(c)]
lic = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        lic[i][j] -= 1

dict0 = {}
dict1 = {}
dict2 = {}
li0 = []
li1 = []
li2 = []

for i in range(n):
    for j in range(n):
        color = lic[i][j]
        if (i+j) % 3 == 0:
            if color in dict0:
                dict0[color] += 1
            else:
                dict0[color] = 1
                li0.append(color)
        elif (i+j) % 3 == 1:
            if color in dict1:
                dict1[color] += 1
            else:
                dict1[color] = 1
                li1.append(color)
        else:
            if color in dict2:
                dict2[color] += 1
            else:
                dict2[color] = 1
                li2.append(color)


ans = 10 ** 10

for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and j != k and k != i:
                ans_tmp = 0
                for ii in li0:
                    if ii != i:
                        ans_tmp += d[ii][i] * dict0[ii]
                for jj in li1:
                    if jj != j:
                        ans_tmp += d[jj][j] * dict1[jj]
                for kk in li2:
                    if kk != k:
                        ans_tmp += d[kk][k] * dict2[kk]
                ans = min(ans, ans_tmp)

print(ans)
