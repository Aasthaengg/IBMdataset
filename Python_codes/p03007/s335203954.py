import collections
N = int(input())
A = list(map(int, input().split()))
A.sort()
A2 = collections.deque(A)
#print(N, A)
x = [0] * (N-1)
y = [0] * (N-1)
for i in range(N -1):
    amin = A2.popleft()
    amax = A2.pop()
    mainasuflag = 0
    plusflag = 0
    if i != N - 2:
        if A2[0] > 0:
            mainasuflag = 1
        if A2[len(A2) - 1] < 0:
            plusflag = 1
        amin2 = abs(A2[0])
        amax2 = abs(A2[len(A2) -1])
        if i == N - 3:
            if A2[0] > 0:
                A2.appendleft(amin - amax)
                x[i] = amin
                y[i] = amax
            else:
                A2.append(amax - amin)
                x[i] = amax
                y[i] = amin
        else:
            if mainasuflag == 1:
                A2.appendleft(amin - amax)
                x[i] = amin
                y[i] = amax
            elif plusflag == 1:
                A2.append(amax - amin)
                x[i] = amax
                y[i] = amin
            else:
                if amax2 >= amin2:
                    A2.appendleft(amin - amax)
                    x[i] = amin
                    y[i] = amax
                else:
                    A2.append(amax - amin)
                    x[i] = amax
                    y[i] = amin

    else:
        A2.append(amax - amin)
        x[i] = amax
        y[i] = amin

    #print("A", A2, mainasuflag, plusflag)

print(A2[0])
#print(x, y)
for i in range(N - 1):
    print(x[i], y[i])