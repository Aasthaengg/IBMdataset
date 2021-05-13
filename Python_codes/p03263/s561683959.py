def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    n = []
    for i in range(h):
        for j in range(w):
            if a[i][j]%2==1:
                flg=0
                if i<h-1:
                    if a[i+1][j]%2==1:
                        a[i+1][j]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+2,j+1])
                        flg=1
                elif 0<i:
                    if a[i-1][j]%2==1:
                        a[i-1][j]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i,j+1])
                        flg=1
                elif j<w-1:
                    if a[i][j+1]%2==1:
                        a[i][j+1]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+1,j+2])
                        flg=1
                elif 0<j:
                    if a[i][j-1]%2==1:
                        a[i][j-1]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+1,j])
                        flg=1
                if flg==0:
                    if i<h-1:
                        a[i+1][j]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+2,j+1])
                    elif j<w-1:
                        a[i][j+1]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+1,j+2])
                    elif i>0:
                        a[i-1][j]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i,j+1])
                    elif j>0:
                        a[i][j-1]+=1
                        a[i][j]-=1
                        n.append([i+1,j+1,i+1,j])
    print(len(n))
    for i in range(len(n)):
        print(' '.join(list(map(str,n[i]))))

if __name__ == "__main__":
    main()
