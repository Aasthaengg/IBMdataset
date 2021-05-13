import sys
read = sys.stdin.read

N, *AB = map(int, read().split())
AB = list(sorted(zip(*[iter(AB)] * 2)))
print(sum(AB[-1]))