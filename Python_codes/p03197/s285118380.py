N=int(input())
f=0
for i in range(N):
    if int(input())%2!=0:
        f=1
if f==0:
    print("second")
else:
    print("first")
