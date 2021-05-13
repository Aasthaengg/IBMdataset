s=input()
for i in range(1,len(s)):
    ln=len(s)-i
    if ln&1:continue
    if s[:ln//2]==s[ln//2:ln]:
        print(ln)
        exit()