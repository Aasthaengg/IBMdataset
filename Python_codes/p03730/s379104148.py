A,B,C = map(int,input().split())
flag = 0
for k in range(1,B+1):
    if (k*A)%B==C:
        flag = 1
        break
if flag==1:
    print("YES")
else:
    print("NO")