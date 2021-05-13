s = input().lower()
n = 0
while True:
    q = []
    q = input().split()
    if q == ["END_OF_TEXT"]:
        break

    for i in q:
        i = i.lower()
        if s == i:
            n += 1
print(n)