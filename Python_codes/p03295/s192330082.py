n, m = [int(i) for i in input().split()]

ab = [[int(i) for i in input().split()] for _ in range(m)]

ab = sorted(ab, key = lambda x:(x[1],x[0]))

now = ab[0][1] - 1
count = 1

for i in range(m):
    if(now < ab[i][0]):
        now = ab[i][1] - 1
        count += 1

print(count)
