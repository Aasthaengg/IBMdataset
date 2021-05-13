s=input()
alp="".join([chr(i) for i in range(97,97+26)])
if len(s)<26:
    for i in alp:
        if i not in s:
            print(s+i);exit()
else:
    if s=="".join([chr(i) for i in range(97,97+26)][::-1]):
        print(-1)
    else:
        for i in range(25)[::-1]:
            for j in range(i+1,26)[::-1]:
                if s[i]<s[j]:
                    print(s[:i]+s[j]);exit()