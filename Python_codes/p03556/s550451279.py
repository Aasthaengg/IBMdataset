s = input()

n = int(s)

answer = []

x = 1
answer.append(x)

while (x * x <= n):
    x += 1
    answer.append(x * x)

p = answer.pop()
if p == 1:
    print(p)
else:
    ans = answer.pop()
    print(ans)