# codefest 2016, A - signboard
s = input()
r = 'CODEFESTIVAL2016'

count = 0
for el_s, el_r in zip(s, r):
    if el_s != el_r:
        count += 1
print(count)
