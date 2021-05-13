_ = input()
a = list(map(int, input().split()))
for i in range(1, len(a)):
    print(a[-i], end=' ')
print(a[0])

