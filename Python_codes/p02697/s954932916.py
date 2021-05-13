X = str(input())
N = int(X.split(' ')[0])
M = int(X.split(' ')[1])



if N % 2 ==1:

    for i in range(M):
        S = i+1
        T = N-i
        print(S, T)
else:
    for i in range(M):
        if i % 2 == 0:
            S = i//2+1
            T = N-i//2
        else:
            S = N//2-1-i//2
            T = N//2+1+i//2
        print(S,T)
    

