from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a,b=map(int,readline().split())
    
    h=100
    w=100
    ans=[["."]*100 if 0<=i<50 else ["#"]*100 for i in range(100)]
    cnt_b=1
    cnt_w=1
    for i in range(h):
        for j in range(w):
            if i%2==0 and j%2==0 and  ans[i][j]==".":
                if cnt_b<b:
                    ans[i][j]="#"
                    cnt_b+=1
            elif i%2==1 and j%2==0 and ans[i][j]=="#":
                if cnt_w<a:
                    ans[i][j]="."
                    cnt_w+=1

    print(h,w)
    for i in range(h):
        print("".join(ans[i]))

if __name__=="__main__":
    main()