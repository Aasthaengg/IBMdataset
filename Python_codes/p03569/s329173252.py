s = input()
t = ''
for i in range(len(s)):
    if s[i]!='x':
        t += s[i]
for i in range(len(t)):
    if t[i]!=t[-1-i]:
        print(-1)
        break
else:
    ans = 0
    L = []
    R = []
    prevl = -1
    prevr = len(s)
    for i in range(len(s)):
        if s[i]!='x':
            L.append(i-prevl-1)
            prevl = i
        if s[-1-i]!='x':
            R.append(prevr-(len(s)-1-i)-1)
            prevr = len(s)-1-i
    L.append(len(s)-prevl-1)
    R.append(prevr)
    for i in range(len(L)):
        ans += abs(L[i]-R[i])
    print(ans//2)