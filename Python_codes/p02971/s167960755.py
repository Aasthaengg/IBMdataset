n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a, reverse=True)
max_a = max(a)
for x in a:
    if x == max_a:
        print(b[1])
    else:
        print(b[0])