def main():
    N=int(input())
    ans=0
    for i in range(1,N+1):
        m=N//i
        ans+=i*m*(m+1)//2
        #print(i,N//i,m)
    print(ans)

if __name__ == '__main__':
    main()