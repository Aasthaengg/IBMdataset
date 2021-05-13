n = int(input())

if n == 1:
    print("Hello World")
else:
    l = []
    for _ in range(2):
        a = int(input())
        l.append(a)
    print(sum(l))