def linp():return list(map(int,input().split()))

n=int(input())
l=linp()
if max(l)>=sum(l)-max(l):
    print("No")
else:print("Yes")