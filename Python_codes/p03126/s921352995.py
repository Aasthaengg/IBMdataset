n, m = map(int, input().split())
like = [0] * m
for i in range(n):
    ka = list(map(int, input().split()))
    k = ka[0]
    a = ka[1:]
    for j in a:
        like[j-1]+=1

print(like.count(n))