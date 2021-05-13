a = list()
while True:
    a.append(sum(list(map(lambda x: int(x), list(input())))))
    if a[-1] == 0:
        break
for a_ in a[:-1]:
    print(a_)