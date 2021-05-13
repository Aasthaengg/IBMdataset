n = int(input())
ta = [tuple(map(int, input().split())) for _ in range(n)] 

ta_cur = list(ta[0])
for i in range(1, n):
  hi = max(-(ta_cur[0]*-1 // ta[i][0]), -(ta_cur[1]*-1 // ta[i][1]))
  ta_cur[0] = ta[i][0] * hi
  ta_cur[1] = ta[i][1] * hi

print(sum(ta_cur))
