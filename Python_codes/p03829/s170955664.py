n, a, b = map(int, input().split())
x = list(map(int, input().split()))

res = 0
pos = x[0]
for town in x[1:]:
    res += min((town - pos) * a, b)
    pos = town

print(res)