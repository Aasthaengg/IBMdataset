from sys import stdin
n,k = [int(x) for x in stdin.readline().rstrip().split()]

if (n-1)//2 + 1 < k:
    print("NO")
else:
    print("YES")