def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():
    s = input()

    b_count = s.count('B')

    b_to_end_sum = 0
    for i in range(len(s)):
        target = s[i]
        if target == 'B':
            b_to_end_sum += (len(s) - i - 1)

    result = b_to_end_sum - sum([i for i in range(b_count)])
    print(result)

run()

# bbww
# bwdw 1
# wddw 1
# wdwd 1
# wwdd 1
#
# wwwwbbbbwbw
#
# wwwwdddwdwd 2
#
# wwwwddwdwdd 2
#
# wwwwdwdwddd 2
# wwwwwdwdddd 1
# wwwwwwddddd
