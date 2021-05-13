s=int(input())
# b=input()
# c=[]
# for i in range(b):
#     c.append(a[i])
a = list(map(int,input().split()))
#b = list(map(int,input().split()))

c = {i for i in a}  

if len(a)==len(c):
    print("YES")
else:
    print("NO") 