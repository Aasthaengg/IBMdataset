def main():
    N=int(input())
    for k in range(1000):
        if k*(k-1)//2==N:
            print("Yes")
            print(k)
            break
        if k*(k-1)//2>N:
            print("No")
            return
    S=[[0]*(k-1) for _ in range(k)]
    a=1
    for i in range(k-1):
        for j in range(k-i-1):
            S[j][i]=a
            S[k-i-1][i+j]=a
            a+=1
    for s in S:
        print(len(s), *s)

if __name__ == "__main__":
    main()