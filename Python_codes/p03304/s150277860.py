from sys import stdin

n, m, d = [int(x) for x in stdin.readline().rstrip().split()]

if d == 0:
    ans = (m-1)*(1/n)
else:
    ans = (m-1)*2*(n-d)/(n*n)

print(ans)
