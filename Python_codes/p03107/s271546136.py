from collections import Counter
s = input()
S = [int(x) for x in list(str(s))]
if sum(S) == 0 or sum(S) == len(S)*1:
    print(0)
else:
    cnt = Counter(s)
    v = cnt.values()

    print(min(v)*2)

