alp = 'abcdefghijklmnopqrstuvwxyz'
s = input()
if s == alp[::-1]:
    print(-1)
elif len(s) == 26:
    for i in range(len(s)-1,0,-1):
        if s[i] > s[i-1]:
            for j in alp:
                if j not in s[:i] and j > s[i-1]:
                    print(s[:i-1]+j)
                    break
            break
else:
    for i in alp:
        if i not in s:
            print(s+i)
            break
