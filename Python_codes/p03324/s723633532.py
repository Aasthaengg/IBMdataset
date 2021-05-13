# numが100で何回割れるか
def getDevide100Count(num: int):
    n = 0
    while num % 100 == 0:
        num = num / 100 
        n += 1
    return n


d, n = map(int, input().split())
count = 0
i = 0
while count != n:
    i += 1
    if getDevide100Count(i) == d:
        count += 1

print(i)