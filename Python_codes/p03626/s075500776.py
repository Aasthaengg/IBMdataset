N,S1,S2 = open(0).read().split()
N = int(N)
m = 1000000007
if N == 1:
    print(3)
else:
    if S1[0] == S1[1]:
        ans = 6
        count = 2
        state = 'h'
    else:
        ans = 3
        count = 1
        state = 'v'
    while count < N - 1:
        if S1[count] == S1[count+1]:
            if state == 'h':
                ans = (ans*3) % m
            else:
                ans = (ans*2) % m
                state = 'h'
            count += 2
        else:
            if state == 'h':
                state = 'v'
            else:
                ans = (ans*2) % m
            count += 1
    if count == N - 1:
        if state == 'v':
            ans = (ans*2) % m
    print(ans)