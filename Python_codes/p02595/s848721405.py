n, d = map(int, input().split())

d **= 2
print(
    len(list(
        filter(lambda l: l[0]**2 + l[1]**2 <= d, 
               [[int(k) for k in input().split()] for i in range(n)]
        )
    ))
)
