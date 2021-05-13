from sys import stdin
n,k = [int(x) for x in stdin.readline().rstrip().split()]
print(0) if n % k == 0 else print(1)