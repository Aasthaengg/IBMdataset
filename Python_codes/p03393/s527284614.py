s = input()
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
buf = ''
for i in alp:
    if not i in set(s):
        buf = i
        break
if buf:
    print(s+buf)
else:
    c = 1
    for i in range(1,len(s)):
        if s[-i-1]>s[-i]:
            c += 1
        else:break
    if c==26:
        print(-1)
    else:
        for i in sorted(s[-c:]):
            if ord(s[-c-1])<ord(i):
                buf = i
                break
        print(s[:-c-1]+buf)