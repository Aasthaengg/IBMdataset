n = int(input())
a = list(map(int, input().split()))
a.sort()
al = 0
bo = 0
while a:
    al += a.pop(-1)
    if not a:
        break
    bo += a.pop(-1)
print(al-bo)