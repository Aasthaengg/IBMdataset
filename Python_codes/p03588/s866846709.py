N = int(input())
ABL = [list(map(int,input().split())) for _ in range(N)]
ABM = max(ABL, key=lambda x: x[0])
print(ABM[0]+ABM[1])