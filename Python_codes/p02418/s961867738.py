s = raw_input()

p = raw_input()

flag = 0
for i in range (len(s)):
    flag = 0
    for j in range(len(p)):
        if p[j] == s[(i + j) % len(s)]:
            flag += 1

        if flag == len(p):
            break

    if flag == len(p):
        break

if flag == len(p):
    print "Yes"
else:
    print "No"