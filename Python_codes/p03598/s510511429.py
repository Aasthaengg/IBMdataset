#B - Collecting Balls (Easy Version)
N = int(input())
K = int(input())
x = list(map(int,input().split()))

distance = 0
for i in x:#全てのyでの試行
    if abs(i - K) < i:
        distance += 2 * abs(i - K)
    else :
        distance += 2 * i
print(distance)