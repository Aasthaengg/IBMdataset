n = int(input())
Big_lis = []
A = []

for i in range(n):
    lis = []
    a = int(input())
    A.append(a)
    for j in range(a):
        x, y = map(int, input().split())
        lis.append((x, y))
    Big_lis.append(lis)
ANS = 0

for i in range(2 ** n):
    check = bin(i)[2:]
    check = '0' * (n - len(check)) + check
    ans = check.count('1')
    for j in range(n):
        if i >> j & 1:
            for k in range(A[j]):
                if str(check[n - Big_lis[j][k][0]]) != str(Big_lis[j][k][1]):
                    ans = 0
    ANS = max(ANS, ans)
print(ANS)