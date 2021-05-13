K = int(input())
A,B = map(int,input().split())
valid = False
for i in range(A,B+1):
    if i % K == 0:
        valid = True
        break
if valid:
    print("OK")
else:
    print("NG")
