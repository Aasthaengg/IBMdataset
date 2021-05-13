n = int(input())
s = [0]*(n+1)

print(0)
a = input()
if a == "Vacant":
    exit()
s[0] = a
s[n] = a

l = 0
r = n
while True:
    m = (r+l)//2
    print(m)
    a = input()
    if a == "Vacant":
        exit()

    s[m] = a
    if s[l] == s[r]:
        if s[l] == s[m]:
            if (m-l) % 2 == 1:
                r = m
            else:
                l = m
        else:
            if (m-l) % 2 == 1:
                l = m
            else:
                r = m
    else:
        if s[l] == s[m]:
            if(m-l) % 2 == 1:
                r = m
            else:
                l = m
        else:
            if(m-l) % 2 == 1:
                l = m
            else:
                r = m
