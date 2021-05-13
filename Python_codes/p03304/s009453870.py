from sys import stdin
n,m,d = [int(x) for x in stdin.readline().rstrip().split()]
if d == 0:
    ans = (1/n) * (m-1)
    print(ans)
else:
    ans = (2*(n-d)/(n**2)) * (m-1)
    print(ans)