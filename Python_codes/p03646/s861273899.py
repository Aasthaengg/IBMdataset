import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

k = int(readline())
roops = k//50
remains = k%50
ans = [49+roops]*50


for i in range(50-remains):
    ans[i] -= remains
for i in range(50-remains,50):
    ans[i] += 50-remains
print(50)
print(*ans)