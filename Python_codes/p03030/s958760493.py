n = int(input())
base_li = [0]*n

for i in range(n):
    l, p = input().split()
    base_li[i] = [i+1, (l, -int(p))]

sl = sorted(base_li, key=lambda w: w[1])
for c in sl:
    print(c[0])
