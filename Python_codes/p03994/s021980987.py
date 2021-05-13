s=input()
k=int(input())
n=len(s)
s=[s[i] for i in range(n)]
l={"a":26,"b":25,"c":24,"d":23,"e":22,"f":21,"g":20,"h":19,"i":18,"j":17,"k":16,"l":15,"m":14,"n":13,"o":12,"p":11,"q":10,"r":9,"s":8,"t":7,"u":6,"v":5,"w":4,"x":3,"y":2,"z":1}
for i in range(n):
    c=s[i]
    if c=="a":
        continue
    if l[c]>k:
        continue
    k-=l[c]
    s[i]="a"
if k>0:
    k=k%26
    c=s[-1]
    for i in l:
        if l[i]==l[c]-k:
            s[-1]=i
s=''.join(s)
print(s)