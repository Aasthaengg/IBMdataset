from sys import stdin
K, X = [int(x) for x in stdin.readline().rstrip().split()]

if X <= K*500:
    print("Yes")
else:
    print("No")