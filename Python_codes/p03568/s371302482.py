n = int(input())
ls = list(map(int, input().split()))

al = 3 ** n
sub = 1

for i in range(n):
    if ls[i] % 2 == 0:
        sub = sub * 2

print(al - sub)