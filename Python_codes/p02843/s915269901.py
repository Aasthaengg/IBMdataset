x=int(input())

n=-1
for i in range(int(x/105),int(x/100)+1):
    n=i
# print(n)

if 0<=x-100*n<=5*n:
    print("1")
else:
    print("0")