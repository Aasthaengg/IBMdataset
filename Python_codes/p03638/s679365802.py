H,W = list(map(int,input().split()))
N = int(input())
A = list(map(int,input().split()))

A_ = []
for a_idx,a in enumerate(A):
    A_.extend([a_idx+1]*a)

i=0
for w in range(0,len(A_),W):
    i+=1
    ans=A_[w:w+W]
    if i%2 == 0:
        ans.reverse()
    print(' '.join(map(str,ans)))