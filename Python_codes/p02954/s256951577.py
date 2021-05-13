def resolve():
    line = input()
    result = [0] * len(line)

    r_odd = 0
    r_even = 0
    for i in range(len(line)):
        if line[i] == 'L':
            if i % 2 == 0:
                result[i] += r_even
                result[i-1] += r_odd
            else:
                result[i] += r_odd
                result[i-1] += r_even
            r_odd = 0
            r_even = 0
        elif line[i] == 'R':
            if i % 2 == 0:
                r_even += 1
            else:
                r_odd += 1
    l_odd = 0
    l_even = 0
    for i in range(len(line)-1, -1, -1):
        if line[i] == 'R':
            if i % 2 == 0:
                result[i] += l_even
                result[i+1] += l_odd
            else:
                result[i] += l_odd
                result[i+1] += l_even
            l_odd = 0
            l_even = 0
        elif line[i] == 'L':
            if i % 2 == 0:
                l_even += 1
            else:
                l_odd += 1

    print(*result)
    
resolve()