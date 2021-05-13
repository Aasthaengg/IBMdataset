def main():
    n=int(input())
    s=input()
    
    ans=s.count('.')
    t=ans
    for i in range(n):
        if s[i]=='.':
            t-=1
        else:
            t+=1           
        ans=min(ans,t)
    print(ans)
    
if __name__=='__main__':
    main()