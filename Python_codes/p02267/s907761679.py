n=input()
S=input().split()
q=input()
T=input().split()
c=0
for t in T:
    if(t in S):c+=1
print(c)