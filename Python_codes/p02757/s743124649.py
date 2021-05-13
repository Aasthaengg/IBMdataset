N, P = map(int, input().split())
S = list(input())

if P != 2 and P != 5:
    count = [0] * P
    ans = 0
    tmp = 0
    for i in range(N - 1, -1, -1):
        tmp += int(S[i]) * pow(10, (N - 1 - i), P)
        tmp %= P
        ans += count[tmp]
        count[tmp] += 1
    ans += count[0]

    # print (count)
    print (ans)

if P == 2:
    count = 0
    for index, s in enumerate(S):
        if int(s) % 2 == 0:
            count += (index + 1)
    print (count)

if P == 5: 
    count = 0
    for index, s in enumerate(S):
        if int(s) % 5 == 0:
            count += (index + 1)
    print (count)