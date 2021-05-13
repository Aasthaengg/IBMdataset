n = int(input())
apple = list(map(int, input().split()))
count = 0
for i in apple:
    if i%2 != 0:
        pass
    else:
        while i%2 == 0:
            i //= 2
            count += 1
print(count)