def main():
    N=int(input())
    AB=[0]*N
    for i in range(N):
        AB[i]=list(map(int,input().split()))
    AB.sort()
    count=AB[-1][0]
    count+=AB[-1][1]
    print(count)
if __name__=="__main__":
    main()