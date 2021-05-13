

def submit():
    s = input()
    t = input()
    char_set = set(s)
    next_char = {c: -1 for c in char_set}
    char_list = {(c, len(s)): -1 for c in char_set}

    for i in reversed(range(len(s))):
        for c in char_set:
            if c == s[i]:
                char_list[(c, i)] = i
            else:
                char_list[(c, i)] = char_list[(c, i + 1)]
            
    loop = 0
    curr = 0
    for c in t:
        # 実現不可能
        if c not in char_set:
            print(-1)
            return
        if char_list[(c, curr)] < 0:
            loop += 1
            curr = 0
        curr = char_list[(c, curr)] + 1
    print(loop * len(s) + curr)
        

submit()