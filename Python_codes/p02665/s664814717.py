N,*A = map(int, open(0).read().split())
ans = 0
temp = 0


limit = [0] * (N+1)
if N == 0:
    if A[0] == 1:
        print('1')
    else:
        print('-1')
else:
    if A[0] != 0:
        print('-1')
    else:
        limit[0] = 1
        for i in range(1,N+1):
            limit[i] = (limit[i-1]*2) - A[i]
            if limit[i] < 0:
                print('-1')
                break
            elif limit[i] == 0:
                if i < N:
                    print('-1')
                    break
        else:
            for i in range(N+1):
                if i == 0:
                    temp = A[N]
                    ans += temp
                    lower = temp
                elif i < N:
                    temp = min(lower,limit[N-i]) + A[N-i]
                    ans += temp
                    lower = temp
                else:
                    ans += 1
            else:
                print(ans)