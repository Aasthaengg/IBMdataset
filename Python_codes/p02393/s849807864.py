from sys import stdin

arr = [int(n) for n in stdin.readline().rstrip().split()]

arr.sort()

print(" ".join(map(str, arr)))

