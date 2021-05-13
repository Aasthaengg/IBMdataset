import sys
readline = sys.stdin.readline

sx,sy,tx,ty = map(int,readline().split())

xdist = tx - sx
ydist = ty - sy

ans = "R" * xdist + "U" * ydist + "L" * xdist + "D" * ydist

ans += "L" + (ydist + 1) * "U" + "R" * (xdist + 1) + "D"
ans += "R" + (ydist + 1) * "D" + "L" * (xdist + 1) + "U"

print(ans)