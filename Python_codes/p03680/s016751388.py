# ABC065 B:Trained?

N = int(input())
l = []
for _ in range(N):
    a = int(input())
    l.append(a-1)

step = 0
c = 0
while True:
    if step == 1:
        ans = c
        break
    if c > N:
        ans = -1
        break
    else:
        c += 1
        step = l[step]
print(ans)