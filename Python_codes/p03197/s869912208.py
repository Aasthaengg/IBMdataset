N=int(input())
flag=False
for i in range(N):
    a=int(input())
    flag|=a%2



if flag:
    print("first")
else:
    print("second")