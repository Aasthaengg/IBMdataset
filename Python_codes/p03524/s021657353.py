from collections import Counter

S = input()
counter = Counter(S)
if len(counter) == 1:
    k = list(counter.keys())[0]
    if counter[k] > 1:
        print('NO')
    else:
        print('YES')
elif len(counter) == 2:
    # a, b → OK
    # a, a, b, b → NG
    for k in counter.keys():
        if counter[k] != 1:
            print('NO')
            exit()
    print('YES')
else:
    # abcabcb → bacbacb OK
    # abbccc → cabc これのどこにcを追加してもNG
    # abcba → abcab OK
    # aabc → abca OK
    min_v = 10 ** 5
    max_v = 0
    for k in counter.keys():
        min_v = min(min_v, counter[k])
        max_v = max(max_v, counter[k])
    if max_v - min_v > 1:
        print('NO')
    else:
        print('YES')
