w = input()

mode = 1
c_s = 0
ans = 0

for i in w:
#    print(i)
    if i == 'S':
        c_s += 1
    else:
        if c_s > 0:
            ans += 1
            mode = 1
            c_s -= 1

print(len(w)-(2*ans))
