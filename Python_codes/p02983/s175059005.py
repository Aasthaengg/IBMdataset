def main():
    l, r= map(int, input().split())
    if l+1 == r:
        return (l*r) % 2019
    ls = []
    for i in range(l,r+1):
        if i %673 ==0:
            return 0
        ls.append(i%2019)
        
    #print(ls)
    ans =2018
    for a in range(len(ls)):
        for b in range(1,len(ls)-a):
            ans = min(ans, (ls[a]*ls[a+b])%2019) 
    return ans
                

if __name__=='__main__':
    print(main())