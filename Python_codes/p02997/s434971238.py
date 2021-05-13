a,b = map(int,input().split())

S  = (a-1)*(a-2)//2
def solve(x,y,s):
    print(a+s-y-1)
    for i in range(1,a):
        print(1,1+i)
    c = 0
    for i in range(1,a):
        for I in range(i+1,a):
            if c == s-b:exit()
            print(i+1,I+1)
            c+=1
            if c == s-b:exit()
# print(b,S)
if not 0<= b <= S:
    print(-1)
    exit()
else:
    solve(a,b,S)
