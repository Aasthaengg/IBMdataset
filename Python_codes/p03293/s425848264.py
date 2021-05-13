s=input()
t=input()
for i in range(int(len(s))):
    if s==t:
        print("Yes")
        exit()
    else:
        t=t[1:len(t)]+t[:1]
print("No")