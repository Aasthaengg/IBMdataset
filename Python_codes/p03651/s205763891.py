def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if K > max(A):
        print("IMPOSSIBLE")
        exit()
    if K in A:
        print("POSSIBLE")
        exit()

    E = list(map(lambda x:abs(x-K),A))
    E = set(E)
    C = [A[i+1]-A[i] for i in range(N-1)]
    C = set(C)
    D = set(A)
    if E&D:
        print("POSSIBLE")
        exit()

    print("IMPOSSIBLE")
    

if __name__ == "__main__":
    main()
