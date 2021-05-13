s=input()
n=len(s)
a=s.index("A")
for i in range(n):
    if s[n-1-i]=="Z":
        print(n-i-a)
        exit()
    
