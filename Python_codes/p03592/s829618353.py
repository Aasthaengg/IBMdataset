# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

H, W, K = map(int, input().split())
Upper = H//2 if H % 2 == 0 else H//2+1
for h in range(Upper):
    w = (K-W*h)/(H-2*h)
    if int(w) == w and 0 <= w <= W:
        print("Yes")
        exit()
print("No")
