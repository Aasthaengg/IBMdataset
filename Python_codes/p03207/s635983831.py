N = int(input())
p = [int(input()) for _ in range(N)]
max_p = max(p)
max_index = p.index(max_p)

sum = 0
for i in range(N):
    if i == max_index:
        sum += int(p[i]/2)
    else:
        sum += p[i]
print(sum)