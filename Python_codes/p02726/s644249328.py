def main():
    n,x,y = map(int,input().split())
    ans = [0 for i in range(n+1)]
    Map = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j>i:
                dis = min(j-i,abs(x-i)+1+abs(j-y),abs(y-i)+1+abs(j-x))
                ans[dis] +=1
    
    for i in range(1,n):
        print(ans[i])
main()