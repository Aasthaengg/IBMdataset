from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,k=map(int,readline().split())
    a=list(map(int,readline().split()))

    d=dict()
    for i in range(n):
        if a[i] not in d:
            d[a[i]]=1
        else:
            d[a[i]]+=1

    d=list(d.items())
    d.sort(key=lambda x:x[1])
    res=0
    for i in range(len(d)-k):
        res+=d[i][1]

    print(res)
    
if __name__=="__main__":
    main()