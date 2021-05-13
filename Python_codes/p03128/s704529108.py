def main():
    n, m = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = [0,2,5,5,4,5,6,3,7,6]
    c = [[b[i], -i] for i in a]
    c.sort()
    result = [[] for _ in range(n+1)]
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in c:
            if i-j[0] >= 0:
                if dp[i-j[0]] >= 0:
                    dp[i] = dp[i-j[0]] +1
                    break
    c = [[-x[1], x[0]] for x in c]
    c.sort(reverse = True)
    result = []
    i = n
    while i > 0:
        j = 0
        while j < len(c):
            if i-c[j][1] >= 0:
                if dp[i-c[j][1]] + 1 == dp[i]:
                    result.append(c[j][0])
                    i -= c[j][1]
                    j = len(c)
                else:
                    j += 1
            else:
                j += 1
    print(''.join(map(str, result)))
if __name__ =='__main__':
    main()