x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
r.sort()
top_red = p[-x:]
top_green = q[-y:]
final = top_red+top_green+r
final.sort()
print(sum(final[-(x+y):]))