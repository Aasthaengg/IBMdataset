#!/mnt/c/Users/moiki/bash/env/bin/python
# N,M = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
a = [ [ea, e] for e,ea in enumerate(a)]

min_ = min(a)
max_ = max(a)


if min_[0] < 0 and abs(min_[0]) > abs(max_[0]):
    cnt = 0
    for i in range(N):
        if a[i][0] > 0:
            cnt += 1
    cnt += N-1
    print(cnt)

    for i in range(N):
        if a[i][0] > 0:
            print(min_[1] +1, i+1)
    for i in range(N-1, 0,-1):
        print(i+1, i)

    
else:
    cnt = 0
    for i in range(N):
        if a[i][0] < 0:
            cnt += 1

    cnt += N-1
    print(cnt)


    for i in range(N):
        if a[i][0] < 0:
            a[i][0] += max_[0]
            print(max_[1] + 1, i+1)
    for i in range(N-1):
        # a[i+1] = a[i] + a[i+1]
        print(i+1, i+1+1)

            # print(
    
        
    
