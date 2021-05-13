S=input()+'R'
n=len(S)-1
a=[0]*n
r=0
while r<n:
    l=S.find('L',r)
    a[l]+=(l-r)//2
    a[l-1]+=(l-r+1)//2
    r=S.find('R',l)
    a[l]+=(r-l+1)//2
    a[l-1]+=(r-l)//2
print(*a)
