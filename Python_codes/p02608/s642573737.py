N = int(input())

keys = [i for i in range(1, N+1)]
values = [0] * N
count_dict = dict(zip(keys, values))

for x in range(1, 110):
    for y in range(x, 110):
        for z in range(y, 110):
            n = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if n > N:
                break
            if x == y and y == z:
                count_dict[n] += 1
            elif x != y and x != z and y != z:
                count_dict[n] += 6
            else:
                count_dict[n] += 3

for v in count_dict.values():
    print(v)