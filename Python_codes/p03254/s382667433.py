N, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0

a.sort()

for idx, v in enumerate(a):
    if v <= x:
        x -= v
        if idx == N - 1:
            if x == 0:
                count += 1
        else:
            count +=1

print(count)
