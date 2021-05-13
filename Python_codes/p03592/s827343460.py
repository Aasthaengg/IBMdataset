# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

H, W, K = map(int, input().split())
for h in range(H+1):
    for w in range(W+1):
        if (W-w)*h+(H-h)*w == K:
            print("Yes")
            exit()
print("No")
