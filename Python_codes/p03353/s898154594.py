list_S = list(input())
k = int(input())
set_ANS = set()
list_Alph = list(set(list_S))
cnt = 0
list_Alph.sort()

for c in list_Alph:
    q = [i for i, x in enumerate(list_S) if x == c]
    list_M = []
    for i in q:
        l = "".join(list_S[i:])
        list_M.append(l)
    list_M.sort()
    for s in list_M:
        m = list(s)
        for j in range(1,len(m)+1):
            b = "".join(m[:j])
            if b not in set_ANS:
                set_ANS.add(b)
                cnt += 1
                if cnt == k:
                    print(b)
                    exit()

