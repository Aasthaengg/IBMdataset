n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
cnt1=0
cnt2=0
j=1
import itertools
for i in itertools.permutations(range(1,n+1)):
    if list (i)==p:
        a=j
    if list(i)==q:
        b=j
    j+=1
print(abs(a-b))