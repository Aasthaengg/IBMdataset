n = int(input())
a, b = [0, 0]
for i in range(n):
    Taro, Hanako = input().split()
    if Taro > Hanako:
        a += 3
    elif Taro < Hanako:
        b += 3
    else:
        a += 1
        b += 1
print(a, b)