s=' '+input()+' '
for _ in range(int(input())):
    l=input().split()
    o=l[0]
    a=int(l[1])+1; b=int(l[2])+2
    if o=='print': print(s[a:b])
    if o=='reverse': s=s[:a]+s[b-1:a-1:-1]+s[b:]
    if o=='replace': s=s[:a]+l[3]+s[b:]