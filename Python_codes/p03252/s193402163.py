from string import ascii_lowercase
s = input()
t = input()

begin = {c:None for c in ascii_lowercase}
end = {c:None for c in ascii_lowercase}

for idx in range(len(s)):
    sc = s[idx]
    tc = t[idx]
    if begin[sc] is not None and begin[sc] != tc:
        print('No')
        exit()
    if end[tc] is not None and end[tc] != sc:
        print('No')
        exit()
    begin[sc] = tc
    end[tc] = sc

print('Yes')