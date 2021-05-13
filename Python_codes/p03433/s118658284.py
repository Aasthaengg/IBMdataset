N = int(input())
A = int(input())

cnt = N//500
if(N-cnt*500<=A):
    print("Yes")
else:
    print("No")