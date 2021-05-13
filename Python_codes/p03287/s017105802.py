import sys
input = sys.stdin.buffer.readline
from collections import Counter

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    cum = [0]
    
    for num in a:
        cum.append((cum[-1]+num)%M)

    c = Counter(cum)
    ans = 0
    
    for it in c.values():
        ans += (it*(it-1))//2
        
    print(ans)
        
if __name__ == "__main__":
    main()
