s=list(input())
K=int(input())
alp=["a","b","c","d","e","f","g",
"h","i","j","k","l","m","n",
"o","p","q","r","s","t","u",
"v","w","x","y","z"]

for i in range(len(s)):
    n=alp.index(s[i])
    if n!=0 and n+K>=26:
        s[i]="a"
        K-=26-n
    if i==len(s)-1 and K>0:
        n=alp.index(s[i])
        s[i]=alp[(n+K)%26]

for j in s:
    print(j,end="")
print()