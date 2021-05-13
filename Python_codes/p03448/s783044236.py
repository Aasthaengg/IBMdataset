a = int(input())  # 500
b = int(input())  # 100
c = int(input())  # 50
x = int(input())  # objecive

counter = 0
for use_a in range(a + 1):
    if 500 * use_a > x:
        continue
    rest = x - 500 * use_a
    for use_b in range(b + 1):
        if 100 * use_b > rest:
            continue
        rest_c = rest - 100 * use_b
        for use_c in range(c + 1):
            if 50 * use_c != rest_c:
                continue
            counter += 1

print(counter)
