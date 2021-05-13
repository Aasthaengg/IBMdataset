N = int(input())

A = [int(input()) for i in range(N)]

max = sorted(A)[-1]
semi_max = sorted(A)[-2]

if max != semi_max:
    ex = A.index(max)
    
    for i in range(0,ex):
        print(max)
    
    print(semi_max)
    
    for i in range(ex+1,N):
        print(max)

else:
    for i in range(N):
        print(max)