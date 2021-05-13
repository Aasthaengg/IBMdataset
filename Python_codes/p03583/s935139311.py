N = int(input())
flag = 0
for a in range(1,3501):
    if flag ==1:
        break
    for b in range(1,3501):
        if 4*a*b - a*N - b*N != 0:
            if a*b*N // (4*a*b - a*N - b* N) > 0 and a*b*N % (4*a*b - a*N - b* N) ==0:
                c = int(a*b*N / (4*a*b - a*N - b* N))
                print(a, b, c)
                flag = 1
                break