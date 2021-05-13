""" a = list(map(int,input().split()))
b = list(map(int,input().split()))
 """

a = int(input())
c =0

for i in range(1,10):
    if a/i  == a//i and a//i<=9:
        c+=1
        break

if c>=1:
    print("Yes")
else:    
    print("No")