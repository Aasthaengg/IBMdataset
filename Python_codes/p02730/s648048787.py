s=input()
n=len(s)
a=s[0:(n-1)//2]
b=s[(n+3)//2-1:n]
c=a[::-1]
d=b[::-1]
sr=s[::-1]
for i in range(n):
    if s[i]==sr[i]:
        pass
    else:
        print("No")
        exit()
for i in range(len(a)):
    if a[i]==c[i]:
        pass
    else:
        print("No")
        exit()
for i in range(len(b)):
    if b[i]==d[i]:
        pass
    else:
        print("No")
        exit()
print("Yes")