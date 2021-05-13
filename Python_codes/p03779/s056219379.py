x = int(input())

num = 0
i = 0
while num < x:
    i += 1
    num += i
if (num - x) < i:
    print(i)