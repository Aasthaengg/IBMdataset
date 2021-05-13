from sys import stdin
def main():
    #入力
    readline=stdin.readline
    H,W=map(int,readline().split())
    a=[]
    for i in range(H):
        a_i=list(map(int,readline().split()))
        a.append(a_i)

    count=0
    operation=[]
    for y in range(H):
        for x in range(W):
            if a[y][x]%2==1 and x==W-1 and y==H-1:
                pass
            elif a[y][x]%2==1 and x==W-1:
                a[y][x]-=1
                a[y+1][x]+=1
                count+=1
                operation.append([y+1,x+1,y+2,x+1])
            elif a[y][x]%2==1:
                a[y][x]-=1
                a[y][x+1]+=1
                count+=1
                operation.append([y+1,x+1,y+1,x+2])

    print(count)
    for i in range(count):
        print(*operation[i])

if __name__=="__main__":
    main()