s = input()

for i in range(1,len(s)):
    tmp = s[:-i]
    if len(tmp) % 2 == 1:
        continue
    else:
        h = int(len(tmp)/2)
        if tmp[h:] == tmp[:h]:
            print(len(tmp))
            break