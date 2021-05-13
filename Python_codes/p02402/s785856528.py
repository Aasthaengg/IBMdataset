from sys import stdin

stdin.readline()

arr = tuple(int(n) for n in stdin.readline().rstrip().split())

print(min(arr), max(arr), sum(arr))
