s = input()

n = int(s)

answer = 0

for i in range(n):
    p = input().split()
    x = int(p[0])
    y = int(p[1])
    answer += (y - x) + 1

print(answer)