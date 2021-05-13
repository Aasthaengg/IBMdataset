import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B=MI()
    v=LI()
    v.sort(reverse =True)
    a=0#確定分
    b=0#選ぶ選択肢の個数
    L=[]#個数のリスト
    cnt=1
    temp=v[0]
    for i in range(1,N):
        if v[i]!=temp:
            L.append(cnt)
            cnt=1
            temp=v[i]
        else:
            cnt+=1
            
            
    L.append(cnt)
        
    cnt2=0    
    for i in range(len(L)):
        a=cnt2
        cnt2+=L[i]
        if cnt2>A:
            b=L[i]
            break
    temp1=0
    if a!=0:
        temp1=sum(v[:a])/a
    ans1=sum(v[:A])/A
    if a==A:
        b=0
      
    
    def cmb(n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        temp=1
        for i in range(r):
            temp*=(n-i)
            
        for i in range(r):
            temp=temp//(i+1)
            
        return temp
        
        
    ans2=0
    if temp1>ans1:
        ans2=cmb(b,A-a)
    else:
        for i in range(A-a,B-a+1):
            ans2+=cmb(b,i)
        
    print(ans1)
    print(ans2)

main()
