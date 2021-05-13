n = int(input())
Taro, Hanako = 0, 0
for _ in range(n):
    a, b = input().split()
    li = sorted(list((a, b)))
    if a == b:
        Taro += 1
        Hanako += 1
    elif a == li[1]:
        Taro += 3
    else:
        Hanako += 3
print("{} {}".format(Taro,Hanako))