s=list(input())
k=int(input())
for e,i in enumerate(s):
    c=(123-ord(i))%26
    if k>=c:
        s[e]="a"
        k-=c
    else:s[e]=i
l = chr((ord(s[-1])-97+k)%26+97)
print("".join(s[:-1])+l)
