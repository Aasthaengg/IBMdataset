n = int(input())
sq = list(map(int, input().split()))
st = set(sq)
if len(sq) == len(st):
    print('YES')
else:
    print('NO')