s = int(input())

i = 1
a_set = {s}

a_prev = s
while True:
    i += 1
    if a_prev % 2 == 0:
        a = a_prev // 2
    else:
        a = 3 * a_prev + 1
    if a in a_set:
        ans = i
        break
    a_set.add(a)
    a_prev = a

print(ans)