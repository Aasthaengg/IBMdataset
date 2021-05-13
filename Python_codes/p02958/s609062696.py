N = int(input())
p = list(map(int, input().split()))
sorted_p = sorted(p)
flg = False
for i in range(N - 1):
    for j in range(i, N):
        temp_p = p.copy()
        temp = temp_p[i]
        temp_p[i] = temp_p[j]
        temp_p[j] = temp
        if temp_p == sorted_p:
            print('YES')
            flg = True
            break
    if flg:
        break
else:
    print('NO')
