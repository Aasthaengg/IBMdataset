def main():
    N,K = map(int,input().split())
    A = set(map(int,input().split()))
    A = list(A)
    A.sort()
    if K > max(A):
        print("IMPOSSIBLE")
        exit()
    if K in A:
        print("POSSIBLE")
        exit()
    E = set(map(lambda x:abs(x-K),A))
    D = set(A)
    if E&D:
        print("POSSIBLE")
        exit()

    print("IMPOSSIBLE")
    

if __name__ == "__main__":
    main()
