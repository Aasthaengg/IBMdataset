import math
N = int(input())
alst = list(map(int, input().split()))
list.sort(alst, reverse = True)
answer = 0
for i in range(N):
    answer += alst[i] * math.pow(-1, i)
print(int(answer))
