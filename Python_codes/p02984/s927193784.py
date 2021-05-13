N = int(input())
A = list(input().split())
#print(N,"\n", A)
temp = 0
el = 1
for i in range(0,N):
    temp = temp + el*int(A[i])
    el = el * (-1)

if N == 1:
    print(temp)
else:
    print(temp, end=' ')
    C = int(temp/2)
    for i in range(1,N-1):
        curr = int(A[i-1])-C
        #print('{}: '.format(i), end='')
        print(2*curr, end=' ')
        C = curr
    curr = int(A[N-2])-C
    print(2*curr)

