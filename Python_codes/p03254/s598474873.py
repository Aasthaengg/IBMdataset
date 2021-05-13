# AGC 027 A - Candy Distribution Again
N, x = map(int,input().split())
an = list(map(int,input().split()))

ak =[] 
while len(an) > 0:
    ak.append(min(an))
    del an[an.index(min(an))]

count = 0
for i in range(N):
    if x > 0:
        x -= ak[i]
        if i != N-1:
            count += 1
        if i == N-1:
            if x == 0:
                count += 1
            else:
                break
    if x < 0:
        count -= 1
        break

    if x == 0:
        break
print(count)