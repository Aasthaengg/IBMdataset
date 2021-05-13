def main():
    n, m = map(int,(input().split()))
    inlis = []
    lis_1 = []
    lis_n = []

    for _ in range(m):
        a, b = map(int, input().split())
        #print(a, b)
        if a == 1:
            lis_1.append(b)
            #print(lis_1)
        if b == n:
            lis_n.append(a)
            #print(lis_n)
    #print(lis_1, lis_n)
    set_1 = set(lis_1)
    set_n = set(lis_n)
    #print(set_1, set_n)
    if set_1 & set_n:
        #print(set_1 & set_n)
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    
if __name__ == "__main__":
    main()
