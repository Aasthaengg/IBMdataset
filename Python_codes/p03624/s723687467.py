S = set(input())
all_ = []
for i in range(97,123):
    all_.append(chr(i))
sa = list(set(all_) - S)
sa.sort()
if sa:
    print(sa[0])
else:
    print('None')