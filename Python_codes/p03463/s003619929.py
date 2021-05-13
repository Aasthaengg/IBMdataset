N,A,B = map(int,input().split())
if (B-A+1) % 2 != 0 :
    flag = 1
else :
    flag = -1

if flag == 1 :
    ans = "Alice"
elif flag == -1 :
    ans = "Borys"
else :
    ans = "Draw"
print(ans)
