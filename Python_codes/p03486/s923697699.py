s=sorted(input())
t=sorted(input(),reverse=True)
n=min(len(s),len(t))

for i in range(n):
    if ord(s[i])<ord(t[i]):
        print("Yes")
        exit()
    elif ord(t[i])<ord(s[i]):
        print("No")
        exit()
        
if len(s)<len(t):
    print("Yes")
else:
    print("No")