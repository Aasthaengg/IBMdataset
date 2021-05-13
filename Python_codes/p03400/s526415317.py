n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

choco = 0

for e_a in a:
    day = 0
    for i in range(d):
        if day*e_a + 1 == (i+1):
            day += 1
            choco += 1

choco += x
print(choco)
