if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()
    count = 2 * n
    maxDiff = 0

    for i in range(0,n+1):
        diff = 0
        for j in range(i):
            if s[n - i :][j] == t[j]:
                diff+=1
            else:
                break
        if maxDiff < diff:
            maxDiff=diff
    print(count-maxDiff)