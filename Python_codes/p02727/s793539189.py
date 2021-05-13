X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
new_arr = p[:X] + q[:Y] + r
new_arr = sorted(new_arr, reverse=True)
print(sum(new_arr[:X+Y]))