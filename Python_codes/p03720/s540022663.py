c, r = map(lambda x: int(x), input().split())
total = [0] * c
for i in range(r):
    f, s = map(lambda x: int(x), input().split())
    total[f - 1] += 1
    total[s - 1] += 1

for number in total:
    print(number)
    
