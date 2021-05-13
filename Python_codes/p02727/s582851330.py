X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

red = p[:X]
green = q[:Y]

all_apple = red+green+r
all_apple.sort(reverse=True)

print(sum(all_apple[:(X+Y)]))