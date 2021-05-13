N=int(input())
S='abcdefghijklmnopqrstuvwxyz'
A=['a']
for _ in range(N-1):
    now=[]
    for a in A:
        b=sorted(list(a))[-1]
        bi=S.index(b)
        for i in range(bi+2):
            now.append(a+S[i])
    A=now.copy()
A.sort()
for a in A:
    print(a)