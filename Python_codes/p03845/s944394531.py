def ABC_50_B():
    N = int(input())
    T = input().split()
    M = int(input())

    for i in range(len(T)):
        T[i] = int(T[i])

    for i in range(M):
        P,X = map(int,input().split())

        Y = T[P-1]
        T[P-1] = X

        print(sum(T))

        T[P-1] = Y




if __name__ == '__main__':

    ABC_50_B()