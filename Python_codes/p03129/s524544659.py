from sys import stdin
N,K = [int(x) for x in stdin.readline().rstrip().split()]
if len(list(range(1,N+1))[0::2]) >= K:
    print("YES")
else:
    print("NO")