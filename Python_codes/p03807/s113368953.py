num_of_odd = num_of_even = 0
N = int(input())
buff = []
for n in map(int, input().split()):
    #n = int(input())
    if n % 2:
        num_of_odd += 1
    else:
        num_of_even += 1
    buff.append(n)


if num_of_odd:
    if num_of_odd % 2:
        if num_of_odd == 1 and num_of_even == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    pirnt('YES')