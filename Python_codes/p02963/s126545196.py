s = int(input())
if s<=10**9:
    print(0,0,0,1,s,0)
    exit()
bx=10**9
by=1
ay=int(s/(10**9))
while True:
    ax = ay*bx-s
    if ax >= 0 and ax <= 10**9:
        break
    else:
        ay+=1
print(0,0,bx,by,ax,ay)