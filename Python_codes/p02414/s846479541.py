n, m, l = map(int, input().split())

def acq_ab(n):
    a = []
    for i in range(n):
        if i == n:
            break
        ai = list(map(int, input().split()))
        a.append(ai)
    return a

def calc(a, b, n, m, l):
    ans = 0
    for i in range(n):
        for j in range(l):
            for k in range(m):
                ans = ans + a[i][k] * b[k][j]
            if j == l - 1:
                #print("j = {}".format(j))
                print(ans)
            else:
                #print("j = {}".format(j))
                print(ans, end=" ")
            ans = 0
    return 0

#a = [[1, 2], [0, 3], [4, 5]]
#b = [[1, 2, 1], [0, 3, 2]]
#c = calc(a, b, 3, 2, 3)
a = acq_ab(n)
b = acq_ab(m)
calc(a, b, n, m, l)
