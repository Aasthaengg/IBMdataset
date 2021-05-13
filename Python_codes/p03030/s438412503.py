n = int(input())

r = []

for i in range(n):
    city, score = input().split()
    score = int (score)
    r.append((i+1, city, score))

r.sort(key=lambda x:x[2], reverse=True)
r.sort(key=lambda x:x[1])

for i in range(n):
    print(r[i][0])