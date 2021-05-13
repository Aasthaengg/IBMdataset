A,B,C = map(int,input().split())
if(C<=B):
    ans = C+B
elif(C>B):
    if(C-B>A):
        ans = 2*B + A + 1
    elif(C-B<=A):
        ans = 2*B + C - B
print(ans)