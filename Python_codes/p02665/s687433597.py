N = int(input())
A = list(map(int,input().split()))
if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
else:
    saidaiA =[]
    oya = 1
    flag = True
    for i in range(len(A)):
        if oya >= 5*10**13:
            ko = 10**14
        else:
            ko = oya *2
        if i == 0:
            ko = 1
        oya = ko - A[i]
        saidaiA.append(ko)
        if oya < 0:
            flag = False
    ans = 0
    # print(saidaiA)
    motikosi = 0
    for i in range(len(A)):
        if A[-i] + motikosi >= saidaiA[-i]:
            ans += saidaiA[-i]
            motikosi = saidaiA[-i]
        else:
            ans += A[-i] + motikosi
            motikosi = A[-i] + motikosi
    if flag == True:
        print(ans+1)
    else:
        print(-1)