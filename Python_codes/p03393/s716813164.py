s = input()
n = len(s)

li = [False] * 26

for i in range(n):
    s1 = s[i]
    li[ord(s1) - ord('a')] = True

if n != 26:
    for i in range(26):
        if not li[i]:
            s += chr(ord('a') + i)
            print(s)
            exit()

else:
    if s == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    else:
        for i in range(2,27):
            s2 = s[-i:]
            if not all((s2[j] > s2[j+1] for j in range(i-1))):
                s3 = s2[0]
                s2 = list(s2)
                s2.sort()
                for j in range(i):
                    if s2[j] == s3:
                        print(s[:-i] + s2[j+1])
                        exit()
