X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())))[-X:]
q = sorted(list(map(int, input().split())))[-Y:]
r = list(map(int, input().split()))

total = sorted(p + q + r)[::-1]
print(sum(total[:X + Y]))
