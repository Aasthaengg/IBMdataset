N = int(input())
P = [list(map(int,input().split())) for i in range(N)]
P.sort()
print(P[-1][0] + P[-1][1])