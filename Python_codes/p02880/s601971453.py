n=int(input())
s=0
for x in range(1,10):
    for y in range(1, 10):
        if x*y==n:
            s=1
if s==1:
    print("Yes")
else:
    print("No")









