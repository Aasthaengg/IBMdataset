A,B = map(int,input().split())

ans = 0
for i in range(0,2):
    if A > B :
        ans = ans + A
        A = A-1
    else :
        ans = ans + B
        B = B-1

print(ans)
