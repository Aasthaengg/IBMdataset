n = int(input())
t_score, h_score = 0, 0
for i in range(n):
    t, h = input().split()
    if t > h:
        t_score += 3
    elif t < h:
        h_score += 3
    else:
        t_score += 1
        h_score += 1
print(t_score, h_score)