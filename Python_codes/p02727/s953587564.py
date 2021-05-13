x, y, a, b, c = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)[:x]
Q = sorted(list(map(int, input().split())), reverse=True)[:y]
R = sorted(list(map(int, input().split())), reverse=True)
PQL = sorted(P+Q+R, reverse=True)
ans = sum(PQL[:x+y])
print(ans)
