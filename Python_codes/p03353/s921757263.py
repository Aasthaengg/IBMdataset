from collections import deque
s=list(input())
K=int(input())
#max(K)=5でaaaaaはa,aa,aaa,aaaa,aaaaaの順
#よって5文字まで取れば良い
d=deque()
for i in range(len(s)):
    d.append(s[i])
comp=[]
#print(d)
for i in range(len(s)):
    buf=deque()
    for j in range(len(d)):
        v=d.popleft()
        buf.append(v)
        if j<5:
            comp.append("".join(buf))
    d=deque()
    for j in range(len(buf)):
        d.append(buf[j])
    d.popleft()
comp=list(set(comp))
comp.sort()
print(comp[K-1])