s=input()
for i in range(2,len(s)-1,2):
    s=s[:-2]
    if s[:len(s)//2]==s[len(s)//2:]:print(len(s));exit()