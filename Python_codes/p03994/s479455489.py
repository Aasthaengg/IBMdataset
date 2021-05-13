s=list(input())
k=int(input())
n=len(s)

for i in range(n-1):
    t=s[i]
    order=ord(t)-97
    if order==0:
        continue
    elif k>=26-order:
        s[i]='a'
        k-=26-order
    else:
        continue
s[n-1]=chr(97+(ord(s[n-1])-97+k)%26)

print(''.join(s))