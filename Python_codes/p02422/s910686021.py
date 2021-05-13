s = raw_input()
q = input()
a = [raw_input().split() for _ in range(q)]

for i in a:
    op = i[0]
    a = int(i[1])
    b = int(i[2])
    if op == "replace" :
        p = i[3]
        s = s[:a] + p + s[b+1:]
    elif op == "reverse" :
        tmp = s[a:b+1]
        s = s[:a] + tmp[::-1] + s[b+1:]
    elif op == "print" :
        print s[a:b+1]