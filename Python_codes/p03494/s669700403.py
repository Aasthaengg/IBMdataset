n = int(input())
a = list(map(int,input().split()))

minno = 10 ** 9

for x in a:
    cheknow = 0
    while x % 2 == 0:
        x = x / 2
        cheknow += 1
    if cheknow < minno:
        minno = cheknow
print(minno)