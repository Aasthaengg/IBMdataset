if __name__ == '__main__':
    n, k = map(int, input().split())
    ans = 0

    for i in range(n,k+1):
        string = str(i)
        lenI = len(string)
        count = 0
        for j in range(lenI //2 ):
            if string[j] == string[lenI-j-1]:
                count +=1
            if count == lenI //2:
                ans +=1

    print(ans)