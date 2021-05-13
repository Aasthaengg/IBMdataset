def need(a):
    if a=="a":
        return 0
    else:
        return 123-ord(a)

s=list(input())
x=int(input())
i=0
while x>0:
    count=need(s[i])
    if x>=count:
        s[i]="a"
        x-=count
    
    if i==len(s)-1:
        s[i]=chr(ord(s[i])+(x%26))
        x=0
    i+=1
print("".join(s))