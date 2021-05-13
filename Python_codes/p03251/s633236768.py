N,M,X,Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
flag = False
for i in range(X+1,Y+1):
    if max(x) < i and min(y) >= i:
        flag = True
        break
if flag:
    print("No War")
else:
    print("War")