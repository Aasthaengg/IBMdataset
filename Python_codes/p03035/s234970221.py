A,B=map(int,input().split(" "))

Ans=0
if A>=13:
    Ans=B
elif 6<=A<13:
    Ans=B//2
print(Ans)