from operator import itemgetter


n = int(input())
info = [list(map(int, input().split())) for i in range(n)]

info = sorted(info, key = itemgetter(1))
print(info[0][0] + info[0][1])