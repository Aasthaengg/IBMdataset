n, q = list(map(int, input().split()))
works = []
for i in range(n):
    works.append(list(input().split()))

count = 0
while len(works) != 0:
    work = works.pop(0)
    time = int(work[1])
    if time > q:
        count += q
        work[1] = time - q
        works.append(work)
    else:
        count += time
        print(work[0] , count)