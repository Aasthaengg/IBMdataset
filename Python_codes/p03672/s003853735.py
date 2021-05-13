s = str(input())
for i in range(len(s)):
    s=s[:-2]
    if s[:len(s)//2] ==s[len(s)//2:]:
        print(len(s))
        break