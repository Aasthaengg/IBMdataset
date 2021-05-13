x1,y1,x2,y2 = map(int, input().split())
dx = x2-x1
dy = y2-y1
res = [x1-dy+dx, y1+dx+dy, x1-dy, y1+dx]
res_s = [str(r) for r in res]
ans = " ".join(res_s)
print(ans)