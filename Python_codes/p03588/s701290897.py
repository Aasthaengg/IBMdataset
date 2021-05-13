AB = [list(map(int,input().split())) for _ in range(int(input()))]
AB.sort()
print(AB[-1][0]+AB[-1][1])