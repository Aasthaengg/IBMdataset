n=int(input())
a=list(map(int, input().split()))
b=0
for i in a:
    b^=i
print("Yes" if b==0 else "No")