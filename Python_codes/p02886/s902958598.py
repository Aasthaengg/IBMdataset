from itertools import combinations as cmb
n = int(input())
D = list(map(int, input().split()))

ans = 0
for c in cmb(D, 2):
    ans += c[0]*c[1]
print(ans)