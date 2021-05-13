w = input()
w_set = set(w)
w_len = list(w)
for i in w_set:
    if w_len.count(i)%2 != 0:
        print('No')
        break
else:
    print('Yes')