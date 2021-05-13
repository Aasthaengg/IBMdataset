import itertools

numbers = []
while True:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0:
        break
    else:
        numbers.append(n)

for n in numbers:
    num = list(range(1, n[0]+1))
    count = 0
    for i in itertools.combinations(num, 3):
        if sum(i) == n[1]:
            count += 1
    print(count)