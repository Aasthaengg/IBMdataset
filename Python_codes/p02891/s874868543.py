s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s) * k // 2)
else:
    l = []
    tmp = s[0]
    tmp_c = 1
    for i in range(1,len(s)):
        if s[i] == tmp:
            tmp_c += 1
        else:
            l.append(tmp_c)
            tmp_c = 1
            tmp = s[i]
    l.append(tmp_c)
    ans = sum([k*(x//2) for x in l])
    if s[0] == s[-1]:
        a = 1
        tmp = s[0]
        for i in range(1,len(s)):
            if s[i] == tmp:
                a += 1
            else:
                break
        b = 1
        tmp = s[-1]
        for i in s[-2::-1]:
            if i == tmp:
                b += 1
            else:
                break
        ans -= (a//2 + b//2 - (a+b)//2) * (k-1)
    print(ans)