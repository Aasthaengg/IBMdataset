alp = list("abcdefghijklmnopqrstuvwxyz")
s=input()
n=len(s)
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif n<26:
    for i in alp:
        if i not in s:
            print(s+i)
            break
else:
    for i in range(len(s)-1,-1,-1):
        for j in range(ord(s[i])+1,ord('z')+1):
            if chr(j) not in s[:i]:
                print(s[:i]+chr(j))
                exit()