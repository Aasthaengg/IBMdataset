from math import *

if __name__ == '__main__':
    N = int(input())
    s = input().rstrip().split(' ')
    A = [int(elem) for elem in s]

    left = []
    total = sum(A)
    for elem in A:
        left.append(total - elem)
        total -= elem

    active = 1
    route = [min(active-A[0], left[0])]
    if route[0] <= 0: 
        if 0 == N and route[0] == 0:
            pass
        else:
            print(-1)
            exit()

    for i in range(1,N+1):
        active = active*2-A[i]
        route.append(min(active, left[i]))
        #print(route[i])
        if route[i] <= 0: 
            if i == N and route[i] == 0:
                break
            else:
                print(-1)
                exit()

    print(sum(route) + sum(A))