k = int(input())
a, b = map(int, input().split())
c = 0
for i in range(a, b+1):
    if i%k==0:
        c+=1
if c>0:
    print("OK")
else:
    print("NG")