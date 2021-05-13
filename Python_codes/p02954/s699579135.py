
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import bisect
    mod=10**9+7
    S=input()
    N=len(S)
    R=[]
    L=[]
    for i in range(N):
        if S[i]=="R":
            R.append(i)
        else:
            L.append(i)
            
    ans=[0]*N
    
    for i in range(N):
        if S[i]=="R":#右側にある一番近いLを探す，それとの距離の偶奇，で
            num = bisect.bisect_left(L,i)
            ii=L[num]
            d=ii-i
            
            if d%2==0:
                ans[ii]+=1
            else:
                ans[ii-1]+=1
                
        else:
            num = bisect.bisect_left(R,i)
            ii=R[num-1]
            d=i-ii
            if d%2==0:
                ans[ii]+=1
            else:
                ans[ii+1]+=1
                
    print(' '.join(map(str, ans)))
            
            
    
    
    

main()
