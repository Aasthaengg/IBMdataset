from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a,b,c,d,e,f=map(int,readline().split())

    w=[]
    for i in range(0,f+1,100):
        for j in range(0,f+1,100):
            n=a*i+b*j
            if n<=f:
                w.append(n)
    w.sort()

    s=[]
    for i in range(f+1):
        for j in range(f+1):
            n=c*i+d*j
            if n<=f:
                s.append(n)
    s.sort()

    cnt=-1
    res=[0,0]
    for x in w:
        for y in s:
            if x+y>f:
                break

            ma=x//100*e
            if y>ma:
                continue
            
            if (x+y)!=0 and cnt<100*y/(x+y):
                cnt=100*y/(x+y)
                res=[x+y,y]

    print(*res)

if __name__=="__main__":
    main()