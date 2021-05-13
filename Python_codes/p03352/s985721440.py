X = int(input())
count = [1]
for x in range (2,50):
    for y in range (2,10):
        if x ** y <= X:
            count.append(x ** y)
print(max(count))