from sys import stdin

n,a,b = [int(x) for x in stdin.readline().strip().split()]
print(int(n/(a+b))*a+min(n%(a+b), a))