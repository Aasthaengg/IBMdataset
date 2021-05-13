n=int(input())
s=str(n)
array = list(map(int,s))
if sum(array)%9==0:
    print("Yes")
else:
    print("No")