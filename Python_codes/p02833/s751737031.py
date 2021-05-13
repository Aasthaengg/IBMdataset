N = int(input())
a = 10
count = 0
if N%2 == 1:
    print(0)
    exit()
else:
    while a <= N:
        count += N//a
        a *= 5
print(count)