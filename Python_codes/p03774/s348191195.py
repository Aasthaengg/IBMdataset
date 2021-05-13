def main():
    n,m=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(n)]
    cd=[list(map(int,input().split())) for _ in range(m)]
    ans =[]
    for AB in ab:
        m = 10**9
        mza = None
        for i,CD in enumerate(cd):
            d = dist(AB,CD)
            if m > d:
                mza = i+1
                m = d
        ans.append(mza)
    for a in ans:
        print(a)
    
def dist(ab, cd):
    return abs(ab[0]-cd[0])+abs(ab[1]-cd[1])
        
if __name__ == "__main__":
    main()