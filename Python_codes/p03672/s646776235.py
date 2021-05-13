def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():
    S = list(input())

    S = S[:len(S) - 1]

    for target_len in range(len(S) - 1, 1, -1):
        if target_len % 2 == 0:
            mid = target_len // 2
            first = S[:mid]
            second = S[mid:mid + mid]

            if first == second:
                print(target_len)
                return

run()


