import sys
pre_S = input()
S = list(pre_S)

if not ( len(S) == 4 and pre_S.isupper() ): sys.exit()

uniq = set(S)
count = 0
if len(uniq) == 2:
    for I in uniq:
        if S.count(I) == 2: count += 1
print('Yes') if count == 2 else print('No')