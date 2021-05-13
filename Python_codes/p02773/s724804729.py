def abc155c_poll():
    cnt_dict = {}
    n = int(input())
    for i in range(n):
        s = input()
        if s not in cnt_dict.keys():
            cnt_dict[s] = 1
        else:
            cnt_dict[s] += 1

    max_val = max(cnt_dict.values())
    for k in sorted(cnt_dict):
        if cnt_dict[k] == max_val:
            print(k)

abc155c_poll()