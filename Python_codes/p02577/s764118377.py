n=input()
li=list(map(int, n))
sum=0
for i in range(len(li)):
    sum+=li[i]
if sum%9==0:
    print("Yes")
else:
    print("No")