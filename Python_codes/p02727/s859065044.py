X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
eat_p = p[:X]
eat_q = q[:Y]

all_apple = eat_p + eat_q + r
all_apple.sort(reverse=True)

print(sum(all_apple[:X+Y]))