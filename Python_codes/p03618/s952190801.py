a=list(input())

unko=[0]*(ord("z")+1-ord("a"))

for aa in a:
    unko[ord(aa)-ord("a")]+=1
tmp=0
for u in unko:
    tmp+=(u*(u-1))//2

print((len(a)*(len(a)-1))//2-tmp+1)