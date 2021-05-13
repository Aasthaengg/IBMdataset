s = input()

abclist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abcstr = ''.join(abclist)
if s == abcstr[::-1]:
    print(-1)
    exit()
if len(s) != 26:
    for a in abclist:
        if a not in s:
            print(s+a)
            exit()

else:
    i = 25
    while s[i-1] > s[i]:
        i -= 1
        #print(s[i-1], s[i])
    #print(s[i-1], s[i])
    tt = s[i-1]
    ss = list(s[i-1:])
    ss.sort()
    print(s[:i-1]+ss[ss.index(tt)+1])
