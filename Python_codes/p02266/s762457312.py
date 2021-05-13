s = input()
a = []
down = []
a_sum = 0
for i,line in enumerate(s):
    if line == "\\":
        down.append(i)
    elif line == "/" and down:
        j = down.pop()
        a_tmp = i-j
        a_sum += a_tmp
        while a and a[-1][0] > j:
            a_tmp += a.pop()[1]
        a.append([j,a_tmp])

print(a_sum)
print(len(a),*[s for i,s in a])