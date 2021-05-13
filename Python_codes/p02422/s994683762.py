# coding: utf-8
# Here your code !
s = input()
q = int(input())

for i in range(q):
    line = input().split()
    
    if len(line) == 4:
        com,a,b,r = line
        a,b = int(a),int(b)
        s = s[:a] + r + s[b+1:]
    else:
        com,a,b = line
        a,b = int(a),int(b)
        if com == "print":
            print(s[a:b+1])
        else:
            sab = s[a:b+1]
            s = s[:a] + sab[::-1] + s[b+1:]