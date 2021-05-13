n = int(input())
guide = [[i+1, list(int(x) if x.isdigit() else x for x in input().split())] for i in range(n)]
guide = sorted(guide, key = lambda x:(x[1][0],-x[1][1]))

for i in range(n):
    print(guide[i][0])