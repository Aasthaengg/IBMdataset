housecount = int(input())
houseposition = list(map(int,input().split()))

MAX_position = max(houseposition)
min_position = min(houseposition)
print(MAX_position - min_position)