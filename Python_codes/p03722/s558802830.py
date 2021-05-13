N,M= map(int,(input().split()))
line = []
for i in range(M):
    a,b,c = map(int,(input().split()))
    line.append([a-1,b-1,-c])

def Bellman_Ford(S,V,E,distance):
    min_distance = [float("inf")]*V # min_distance[i] は始点から街iまでの最短距離
    min_distance[S-1] = 0 # 始点から始点への最短距離は0とする
    count = 1
    while count < 2*V:
        if count == V:
            tmp = min_distance[N-1]
        count += 1
        for s,g,d in distance: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != float("inf") and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = min_distance[s] + d # 最短距離を上書きする
    return min_distance,tmp

min_distance,ansN = Bellman_Ford(1,N,M,line)
ans2N = min_distance[N-1]
if ansN == ans2N:
    print(-ansN)
else:
    print("inf")