s=sorted(list(input()))
t=sorted(list(input()),reverse=True)
s="".join(s)
t="".join(t)
if s<t:
    print("Yes")
else:
    print("No")
    
