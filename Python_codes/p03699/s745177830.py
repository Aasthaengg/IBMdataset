n = int(input())
apple = []
for _ in range(n):
    apple.append(int(input()))
a = sum(apple)
b = sorted(apple)
count = 0
if str(a)[-1] != "0":
    print(a)
else:
    for i in b:
        c = a
        c -= i
        if str(c)[-1] != "0":
            print(max(c, 0))
            break
        else:
            count += 1
            if count == len(apple):
                print(0)