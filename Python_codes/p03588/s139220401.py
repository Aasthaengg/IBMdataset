import sys
read = sys.stdin.read

N, *AB = map(int, read().split())
AB = max(zip(*[iter(AB)] * 2))
print(sum(AB))