D, N = map(int, input().split())

lst = []
X = "00" * D

for i in range(1,102):
    if i % 100 == 0:
        pass
    else:
        lst.append(str(i) + X)

print(lst[N-1])
