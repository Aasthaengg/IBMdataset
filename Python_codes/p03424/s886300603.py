n=int(input())
list=list(input().split())
ans=0
for i in range(n):
    if "Y" in list[i]:ans=1
print("Three" if ans==0 else "Four")