# coding: utf-8
# Here your code !
N = int(input())

for i in range(N):
    a,b,c = map(int, input().split())
    flg = 0
    if a*a + b*b == c*c:
        flg = 1
    if c*c + a*a == b*b:
        flg = 1
    if b*b + c*c == a*a:
        flg = 1
    if flg == 1:
        print('YES')
    else:
        print('NO')