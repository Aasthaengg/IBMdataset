
def solve():
    gx,gy = False, False
    if W/2 == x:
        gx = True
    if H/2 == y:
        gy = True
    ans = W*H/2
#    print(gx,gy)
    if gx and gy:
        print(ans, 1)
    else:
        print(ans, 0)

    

if __name__ == "__main__":
    W,H,x,y = list(map(float, input().split()))
    solve()  
