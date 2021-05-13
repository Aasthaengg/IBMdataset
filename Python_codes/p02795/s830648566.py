a = [int(input()) for i in range(2)]
b = int(input())

if b % max(a) == 0:
    print(b // max(a))
else:
    print(b // max(a) + 1)