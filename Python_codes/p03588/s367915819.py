from sys import stdin
N = int(stdin.readline().rstrip())
AB = sorted([list(map(int, stdin.readline().rstrip().split())) for _ in range(N)])
print(AB[N-1][0]+AB[N-1][1])