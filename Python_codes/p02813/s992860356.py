import itertools
a = 0
b = 0
cnt = 1
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=sorted(p)
for i in itertools.permutations(r, n):
    if list(i) == p:
        a += cnt
    if list(i) == q:
        b += cnt
    if a!=0 and b!=0:
        break
    else:
        cnt += 1
    
print(abs(a-b))