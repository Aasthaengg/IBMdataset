N=int(input())
S=input()
slst=[s for s in S]
Q=int(input())

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
bits=[Bit(N) for _ in range(26)]

for i in range(N):
    ch=ord(S[i])-ord('a')
    bits[ch].add(i+1,1)

for _ in range(Q):
    t,a,b=input().split()

    if t=='1':
        a=int(a)
        pos=a-1
        nextc=ord(b)-ord('a')
        beforec=ord(slst[pos])-ord('a')

        if nextc!=beforec:
            bits[beforec].add(a,-1)
            bits[nextc].add(a,1)
            slst[pos]=b
            
    else:
        l=int(a)
        r=int(b)

        cnt=[0]*26

        for i in range(26):
            cnt[i]+=bits[i].sum(r)
        
        if l-1>0:
            for i in range(26):
                cnt[i]-=bits[i].sum(l-1)
        
        ans=0

        for i in range(26):
            if cnt[i]>0:
                ans+=1
        
        print(ans)
