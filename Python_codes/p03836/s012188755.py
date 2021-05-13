import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


sx,sy,tx,ty = map(int, input().split())
wx = tx-sx
wy = ty-sy
ans = "U"*wy + "R"*wx + "D"*wy + "L"*wx + ("L"*1 + "U"*(wy+1) + "R"*(wx+1) + "D"*1) + ("R"*1 + "D"*(wy+1) + "L"*(wx+1) + "U"*1)
print(ans)