def main():
    n = int(input())
    M = 55555
    Int = [i for i in range(M+1)]
    for i in range(2,len(Int)):
        if Int[i]!=0:
            for k in range(2,M//Int[i]):
                Int[i*k] = 0
    prm = []
    for i in Int:
        if i!=0 and i%5==1:
            prm.append(i)
    prm = prm[1:]
    print(' '.join([str(x) for x in prm[0:n]]))

if __name__ == "__main__":
    main()
