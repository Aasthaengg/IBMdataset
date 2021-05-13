import itertools

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

seq = []
for i in range(1,n+1):
    seq.append(i)
pat = list(itertools.permutations(seq))

ans = 0
cnt = 0
for i in range(len(pat)):
    if pat[i]==p or pat[i]==q:
        if p==q:
            print(0)
            break
        if cnt==1:
            print(i-ans)
            break
        ans = i
        cnt = 1