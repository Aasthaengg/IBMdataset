def main():
    R,G,B,N=map(int,input().split())
    cnt=0
    for r in range(0,N//R+1):
        for g in range(0,(N-r*R)//G+1):
            bunshi=N-r*R-g*G
            q,m=divmod(bunshi,B)
            # if q<0:continue
            if m==0:cnt+=1
    print(cnt)
main()