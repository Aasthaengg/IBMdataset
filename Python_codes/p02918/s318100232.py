def ma():
    return map(int,input().split())

def main():
    n,k=ma()
    b=input()
    left=0
    for i in range(n-1):
        if b[i]==b[i+1]:
            left+=1
    ans=min(left+2*k, n-1)
    print(ans)

if __name__=='__main__':
    main()    