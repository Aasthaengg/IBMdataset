def resolve():

    n=int(input())
    H=list(map(int,input().split()))
    def main():
        if n == 1:
            return 'Yes'
        maxval=0
        for i in range(n):
            if maxval-2>=H[i]:
                return 'No'
            else:
                maxval=max(maxval,H[i])
        return 'Yes'
    print(main())


resolve()
