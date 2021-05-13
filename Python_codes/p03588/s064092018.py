from sys import stdin

n = int(stdin.readline().rstrip())
li = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]

li.sort()

print(sum(li[-1]))