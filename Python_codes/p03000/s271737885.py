N,X = map(int,input().split())
l = list(map(int, input().split()))

d = 0
count = 1

for i in range(N):
    d = d + l[i]
    if d <= X:
        count += 1

print(count)