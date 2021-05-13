import sys
input = sys.stdin.readline
n, h = map(int, input().split())
ab = []
for i in range(n):
  a, b = map(int, input().split())
  ab.append((-a, b, i))
  
ab.sort()
index = ab[0][2]
ai = -ab[0][0]
bi = ab[0][1]

ab2 = ab[:]
ab2.sort(key = lambda x:x[1], reverse = True)

cnt = 0

for a, b, i in ab2:
    if i == index:
        continue
    if b < ai:
        break
    if h <= bi:
        print(cnt+1)
        sys.exit()
    h -= b
    cnt += 1
    if h <= 0:
        print(cnt)
        sys.exit()


print(cnt + 1 +  max(0, h - bi + ai - 1) // ai)