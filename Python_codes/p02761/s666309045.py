N, M = map(int, input().split())
s = []
c = []
if M == 0:
    if N != 1:
        print(10**(N-1))
    else:
        print(0)
else:   
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    if N != 1:
        for i in range(10**(N-1), 10**N):
            for j in range(M):
                if str(i)[s[j]-1] != str(c[j]):
                    break
                if j == M - 1:
                    print(i)
                    c = 1
                    break
            if c == 1:
                break
            if i == 10**N -1:
                print(-1)
    else:
        for i in range(0, 10):
            for j in range(M):
                if str(i)[s[j]-1] != str(c[j]):
                    break
                if j == M - 1:
                    print(i)
                    c = 1
                    break
            if c == 1:
                break
            if i == 10**N -1:
                print(-1)