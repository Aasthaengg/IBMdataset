x = list(map(int, input().split()))
y = list(range(1,6))
for i in y:
    if i not in x:
        print(i)
        break