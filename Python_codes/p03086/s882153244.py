def abc122b_atcoder():
    s = input()
    cnt = 0
    max_val = 0
    for c in s:
        if c in ['A', 'C', 'G', 'T']:
            cnt +=1
        else:
            max_val = max(max_val, cnt)
            cnt = 0
    max_val = max(max_val, cnt)
    print(max_val)
abc122b_atcoder()