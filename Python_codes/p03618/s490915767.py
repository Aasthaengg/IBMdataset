def main():
    A=input()
    N=len(A)
    ans=1
    p={}
    for i,a in enumerate(A):
        if a not in p:
            p[a]=0
        ans+=i-p[a]
        p[a]+=1    
    print(ans)

if __name__ == "__main__":
    main()