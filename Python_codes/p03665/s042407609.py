from math import factorial

n,p=map(int,input().split())
a=list(map(int,input().split()))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

ev=len(even)
od=len(odd)
odd_sum=0

for i in range(od+1):
    if i%2==p and i<=od:
        odd_sum+=(factorial(od)//(factorial(od-i)*factorial(i)))

print(odd_sum*(2**ev))