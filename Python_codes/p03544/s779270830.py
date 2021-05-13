def ABC_79_B():
    N=int(input())
    l = [0 for _ in range(N*2)]
    l[0]=2
    l[1]=1

    for i in range(N-1):
        if N==1:
            print(l[1])
            break
        else:
            l[i+2] = l[i]+l[i+1]

    print(l[N])

if __name__ == '__main__':

    ABC_79_B()