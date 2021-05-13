h = input()
h = list(h)
hoge = 0
for i in h:
    if i == '+':
        hoge += 1
    else:
        hoge -= 1

print(hoge)
