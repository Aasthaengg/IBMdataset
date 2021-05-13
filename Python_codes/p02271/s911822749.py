n = input()
A = map(int, raw_input().split())
q = input()
m = map(int, raw_input().split())

a = [[0 for j in range(max(m) + 1)] for i in range(n)]

for i in range(n):
    for j in range(max(m) + 1):
        if (i == 0):
            temp = A[i]
            if (temp <= j):
                a[i][j] = temp
            else:
                a[i][j] = 0
        else:
            temp1 = 0
            temp2 = 0
            if (j - A[i] >= 0):
                temp1 = a[i-1][j - A[i]] + A[i]
            temp2 = a[i-1][j]
            a[i][j] = max(temp1, temp2)

for i in range(q):
    if (a[n-1][m[i]] == m[i]):
        print "yes"
    else:
        print "no"