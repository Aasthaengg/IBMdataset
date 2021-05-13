n = int(input())
rates = set()
over = 0
people = list(map(int, input().split()))
for rate in people:
    if rate // 400 >= 8:
        over += 1
    else:
        rates.add(rate // 400)
print(max(1, len(rates)), len(rates) + over)