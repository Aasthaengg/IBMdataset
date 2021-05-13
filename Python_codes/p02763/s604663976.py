class segtree:
    def __init__(self,N):
        self.n=(1<<len(bin(N-1)[2:]))
        self.x=[0 for _ in range(2*self.n)]
    def build(self,seq):
        for i, j in enumerate(seq, start=self.n):
            self.x[i]=1<<j
        for i in range(self.n-1, 0, -1):
            self.x[i]=self.x[i*2]|self.x[i*2+1]
    def update(self, i, c):
        j=i+self.n
        self.x[j]=1<<c
        while j>1:
            j//=2
            self.x[j]=self.x[j*2]|self.x[j*2+1]
    def get(self,l,r):
        ans=0
        l+=self.n
        r+=self.n
        while l<r:
            if l%2==1:
                ans|=self.x[l]
                l+=1
            if r%2==0:
                ans|=self.x[r]
                r-=1
            l//=2
            r//=2
        if l==r:
            ans|=self.x[l]
        cnt=sum(list(map(int, list(bin(ans)[2:]))))
        print(cnt)
        
n=int(input())
s=list(input())
s=[ord(i)-97 for i in s]
seg=segtree(n)
seg.build(s)
#print(seg.x)
for _ in range(int(input())):
    que=list(input().split())
    if que[0]=='1':
        seg.update(int(que[1])-1, ord(que[2])-97)
    elif que[0]=='2':
        seg.get(int(que[1])-1,int(que[2])-1)