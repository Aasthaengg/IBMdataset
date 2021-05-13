A, B, K = map(int, input().split())

lst = []

for i in range(K):
    if A + i <= B:
        lst.append(A+i)
    else:
        break

for j in range(K):
    if A <= B - j:
        lst.append(B-j)
    else:
        break

lst = sorted(list(set(lst)))

for l in lst:
    print(l)
