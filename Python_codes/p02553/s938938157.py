# --------- B -----------
a, b, c, d = map(int, input().split())
answer = max(a*c, a*d, b*c, b*d)
print(answer)