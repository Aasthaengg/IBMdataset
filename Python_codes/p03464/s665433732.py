K = int(input())
S = list(map(int, input().split()))

m = [0]*K
M = [0]*K
m[K-1] = 2
M[K-1] = 3
if S[K-1] != 2:
    print(-1)
else:
    for i in range(K-2, -1, -1):
        if m[i+1]%S[i] == 0:
            m[i] = m[i+1]
        else:
            m[i] = m[i+1]+S[i]-(m[i+1]%S[i])
        if M[i+1]%S[i] == 0:
            M[i] = M[i+1]+S[i]-1
        else:
            M[i] = (M[i+1]//S[i])*S[i]+S[i]-1
        if m[0] > M[0]:
            print(-1)
            break
    else:
        print(m[0], M[0])
