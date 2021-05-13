n = int(raw_input())
S = map(int,raw_input().strip().split(' '))

comp = 0

def merge_sort(S):
    if len(S) <= 1:
        return S
    S1,S2 = split(S)
    return merge(merge_sort(S1),merge_sort(S2))

def split(S):
    mid = len(S)/2
    return S[:mid],S[mid:]

def merge(S1,S2):
    S = []
    S1.append(100000000000)
    S2.append(100000000000)
    global comp
    i = 0
    j = 0
    for k in range(len(S1)+len(S2)-2):
        comp += 1
        if S1[i] <= S2[j]:
            S.append(S1[i])
            i += 1
        else:
            S.append(S2[j])
            j += 1
    return S

sorted_S = merge_sort(S)
for s in sorted_S:
    print s,
print
print comp