from collections import Counter
N,*A = map(int,open(0).read().split())
ca = Counter(A)
copy_ca = ca.copy()
for i in ca.items():
    if i[1] % 2 == 0:
        del copy_ca[i[0]]
print(len(copy_ca))        