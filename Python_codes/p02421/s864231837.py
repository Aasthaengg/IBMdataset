i = int(input())

tarou = 0
hanako = 0

for x in range(i):
    a,b = input().split()
    if b > a:
        hanako += 3
    elif a > b:
        tarou += 3
    else:
        hanako += 1
        tarou += 1
print("{0} {1}".format(tarou, hanako))