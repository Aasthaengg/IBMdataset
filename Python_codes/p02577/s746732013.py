n=str(input())
A=0
for i in range(len(n)):
    A += int(n[i])
if A%9==0:
    print('Yes')
else:
    print('No')