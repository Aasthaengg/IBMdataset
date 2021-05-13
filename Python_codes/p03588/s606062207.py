N = int(input())

member = {}
min_score = 10**9
for i in range(N):
    a, b = [int(x) for x in input().split()]
    member[b] = a

    if min_score > b:
        min_score = b

last = member[min_score]
print(last + min_score)
