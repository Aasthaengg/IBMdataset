n = int(input())
pos = list(map(int, input().split(' ')))

assert n == len(pos)

print(max(pos)-min(pos))