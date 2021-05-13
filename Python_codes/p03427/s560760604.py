n = list(input())
if len(n) == 1:
    print(n[0])
    exit()
n = [int(n[i]) for i in range(len(n))]
m = set(n[1:])
if m == {9}:
    print(sum(n[1:]) + n[0])
    exit()
else:
    print(9*(len(n)-1) + n[0] -1)