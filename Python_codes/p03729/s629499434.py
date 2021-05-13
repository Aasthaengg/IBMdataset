num_a, num_b, num_c = map(str, input().split())

if num_a[-1] == num_b[0] and num_b[-1] == num_c[0]:
    print('YES')
else:
    print('NO')