# your code goes here
#linear
n=int(input())
S=[int(i) for i in input().split()]
q=int(input())
T=[int(i) for i in input().split()]
c=0
for i in range(q):
    j=0
    while j<n and T[i]!=S[j]:
        j+=1
    if j<n:
        c+=1
print(c)