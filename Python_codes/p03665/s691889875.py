from math import factorial
n,p=map(int,input().split())
a=list(map(int,input().split()))
a1=[]
a0=[]

for i in a:
    if i%2==1:
        a1.append(i)
    else:
        a0.append(i)

a1c=len(a1)
a0c=len(a0)
#print(a1)
#print(a0)
ans1=0
for i in range(a0c+1):
    ans1+=factorial(a0c) / factorial(i) / factorial(a0c - i)
#print(ans1)
ans2=0
if p==1:
    for i in range(1,a1c+1,2):
        ans2+=factorial(a1c) / factorial(i) / factorial(a1c - i)

else:
    for i in range(0,a1c+1,2):
        ans2+=factorial(a1c) / factorial(i) / factorial(a1c - i)

print(int(ans2*ans1))