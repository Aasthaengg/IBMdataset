d="zyxwvutsrqponmlkjihgfedcba"
s=input()
if s=="zyxwvutsrqponmlkjihgfedcba":print(-1)
else:
    if len(s)!=26:
        for i in range(1,1+26):
            if d[-i] not in s:print(s+d[-i]);exit()
    else:
        from bisect import bisect_left as bl,bisect_right as br
        de=[s[-1]]
        for i in range(2,27):

            if de[-1]<s[-i]:de.append(s[-i])
            else:print(s[:-i]+de[bl(de,s[-i])]);exit()