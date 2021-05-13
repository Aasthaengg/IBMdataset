K = int(input())
a,b = map(int,input().split())
count = 0
for i in range(a,b+1):
    if i % K == 0:
        count += 1
if count == 0:
    print("NG")
else:
    print("OK")