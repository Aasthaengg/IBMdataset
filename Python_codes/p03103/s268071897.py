def main():
    n, m= map(int, input().split()) 
    inlis = list()
    for i in range(n):
        a, b = list(map(int, input().split()))
        inlis.append([a,b])
    inlis.sort(key = lambda x: x[0])
    #print(inlis)

    tmp = 0
    kane = 0

    for numlis in inlis:
        a = numlis[0]
        b = numlis[1]

        if tmp + b <= m:
            tmp += b 
            kane += a * b
        
        else:
            kau = m - tmp
            tmp += kau
            kane += a * kau

        if tmp == m:
            break
    print(kane)   


if __name__ == "__main__":
    main()