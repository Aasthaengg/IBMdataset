# PROXY

N = int(input())
A = list(input() + input() + input())
counter = 0
time = 0
while counter < N:
    if A[counter] == A[counter + N] and A[counter] == A[counter + N*2]:
        time += 2
        counter += 1
    elif A[counter] == A[counter + N]:
        time += 1
        counter += 1
    elif A[counter] == A[counter + N*2]:
        time += 1
        counter += 1
    elif A[counter + N] == A[counter + N*2]:
        time += 1
        counter += 1
    else:
        time += 0
        counter += 1
print(2*N - time)