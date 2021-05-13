# ABC 073: B – Theater
n = int(input())
groups = [[int(s) for s in input().split()] for _ in range(n)]
members = [groups[i][1] - groups[i][0] + 1 for i in range(n)]
print(sum(members))