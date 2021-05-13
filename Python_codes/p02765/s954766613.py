n,r = list(map(int, input().split()))

if n < 10:
    inside_score = r + 100*(10 - n)
    print(inside_score)
else:
    print(r)