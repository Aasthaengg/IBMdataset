d = list(map(int, open(0)))
k = d.pop()
for s in d:
    for t in d:
        if abs(s-t) > k:
            print(':(')
            exit()
print('Yay!')
