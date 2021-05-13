s=list(input())
if len(s)==2:
    for i in range(2):
        print(s[i],end="")
else:
    s.reverse()
    for i in range(3):
        print(s[i],end="")