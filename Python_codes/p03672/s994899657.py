S=input()
for i in range(len(S)):
    s=S[:len(S)-i-2]
    if len(s)%2==0:
        if s[:len(s)//2]==s[len(s)//2:]:print(len(s));break