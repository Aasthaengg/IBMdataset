s=input()
k=int(input())
st=[[] for i in range(26)]
n=len(s)
for i in range(n):
    st[ord(s[i])-97].append(i)

pre=0
now=set()
for i in st:
    for v in i:
        for c in range(v+1,min(n+1,v+6)):
            now.add(s[v:c])
    if len(now)+pre<k:pre+=len(now);now=set()
    else:
        print(sorted(list(now))[k-pre-1]);exit()