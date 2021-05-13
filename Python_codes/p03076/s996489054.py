a = [int(input()) for _ in range(5)]
if all(i % 10 == 0 for i in a):
    print(sum(a))
else:
    b = sum(i // 10 for i in a) * 10
    c = [i % 10 for i in a if i % 10 != 0]
    print(b + len(c) * 10 - (10 - min(c)))