import sys

n=input()
test=list(set(n))
#print(test)
if len(test)==1 and test[0]=="7":
    print(len(n))
    sys.exit()
n=int(n)
if n==1:
    print(1)
    sys.exit()
if n%2 ==0:
    print(-1)
    sys.exit()

Ai=[7%n]
for i in range(1,n+1):
    res=(Ai[i-1]*10 + 7)%n
    if res ==0:
        print(i+1)
        sys.exit()
    Ai.append(res)
print(-1)