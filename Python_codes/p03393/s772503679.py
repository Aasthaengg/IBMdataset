s = input()
if len(set(s))==26:
    for i in range(26):
        for j in range(i+1):
            if s[-(i+1)]<s[-(j+1)]:
                print(s[:-(i+1)]+s[-(j+1)]);exit()
    else:
        print(-1);exit()
else:
    chr_li = [ord(chr_) for chr_ in s]
    for i in range(97,97+26):
        if i not in chr_li:
            print(s+chr(i));exit()