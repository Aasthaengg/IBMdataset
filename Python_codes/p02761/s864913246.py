import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())


    S =[]
    C=[]
    for i in range(M):
        s,c=map(int,input().split())
        S.append(s)
        C.append(c)

    mini = 10**(N-1)
    if N==1:
        mini=0

    for i in range(mini,10**N):
        j = str(i)
        for k in range(M):
            s,c =S[k],C[k]
            if j[s-1]!=str(c):
                break
        else:
            print(i)
            exit()

    print(-1)






if __name__ == "__main__":
    main()
