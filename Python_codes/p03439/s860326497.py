N=int(input())

l = 0
r = N-1
print(l)
t = input()
if t=='Vacant': exit()
for i in range(20-1):
    q = (l+r)//2
    if l==q:
        print(l+1)
        exit()
    print(q)
    s = input()
    if s=='Vacant': exit()
    if ((q-l)&1==0 and s==t) or ((q-l)&1==1 and s!=t):
        l=q
        t=s
    else:
        r=q-1
