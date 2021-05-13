H,N=(map(int,input().split()))
a1=input().split()
a2=[int(i) for i in a1]
x=0
for i in a2:
    x+=i
print('Yes' if x>=H else 'No')
