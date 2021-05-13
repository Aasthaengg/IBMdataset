import sys
input = sys.stdin.buffer.readline
import bisect

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    
    a.sort()
    cum = [0]
    for num in a:
        cum.append(cum[-1]+num)
    
    def power(x):
        count = 0
        for num in a:
            rest = x-num
            index = bisect.bisect_left(a,rest)
            count += N-index
        if count >= M:
            return True
        else:
            return False
    
    l,r = -1,10**10
    while r-l > 1:
        mid = (r+l)//2
        if power(mid):
            l = mid
        else:
            r = mid
            
    border = r
    
    count,ans = 0,0
    for num in a:
        rest = border-num
        index = bisect.bisect_left(a,rest)
        ans += (N-index)*num
        ans += cum[N]-cum[index]
        count += N-index
        
    print(ans+(M-count)*l)
        

if __name__ == "__main__":
    main()
