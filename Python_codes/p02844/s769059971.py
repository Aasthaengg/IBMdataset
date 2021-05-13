N = int(input())
S = input()
res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            tnp = [i,j,k]
            flag = 0
            for s in S:
                if int(s) == tnp[flag]:
                    flag += 1
                if flag == 3:
                    res += 1
                    break
print(res)