n, m = list(map(int, input().split()))

like = [True] * (m+1)

for i in range(n):
    ka = list(map(int, input().split()))
    for j in range(1, m+1):
        if j not in ka[1:]:
            like[j] = False

print(like[1:].count(True))
        
