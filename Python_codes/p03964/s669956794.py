from sys import stdin

n = int(stdin.readline().rstrip())
li = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
A,B = li[0][0],li[0][1]
for i in range(1,n):
    a,b = li[i][0],li[i][1]
    bai = max(-(-A//a),-(-B//b))
    A = bai*a
    B = bai*b
print(A+B)