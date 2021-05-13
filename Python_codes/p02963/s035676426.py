def main(s):
    #s=10**17-0
    a=10**9
    if s<=10**9:
        x1,y1,x2,y2,x3,y3=0,0,s,0,0,1
    elif s%a==0:
        x1,y1,x2,y2,x3,y3=0,0,a,0,a,s//a
    else:
        x1,y1=0,0
        x2,y2=s//a+1,a-s%a
        x3,y3=1,a
    print(x1,y1,x2,y2,x3,y3)
if __name__=='__main__':
    s=int(input())
    main(s)