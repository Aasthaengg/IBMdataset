n,m = map(int,input().split())
li=list(map(int,input().split()))
if n>sum(li):
    print("No")
else:
    print("Yes")