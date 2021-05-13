def main():
    n=int(input())
    num=[i*(i+1)//2 for i in range(4473)]
    ans=[]
    while n>0:
        for i in range(1,4473):
            if num[i]>=n:
                ans.append(i)
                n-=i
                break
    for i in range(len(ans)):
        print(ans[len(ans)-1-i])
if __name__=="__main__":
    main()