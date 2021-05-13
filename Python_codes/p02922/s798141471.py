import sys
A,B=map(int,input().split())
num=A
cnt=1
if B==1:
    print(0)
    sys.exit()
while num<B:
    cnt+=1
    num+=A-1

print(cnt)

