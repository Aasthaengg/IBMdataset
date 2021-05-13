n = int(input())
i = 0
#list_n = [n]

map_n = map(int, input().split())
list_n = list(map_n)

min = min(list_n)
max = max(list_n)
sum = sum(list_n)

print("%d %d %d" % (min, max, sum))