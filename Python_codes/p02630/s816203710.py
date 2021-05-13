from collections import Counter

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    c = Counter(a)
    allsum = 0
    for k,v in c.items():
        allsum += k*v
    ans = []
    for i in range(q):
        bi,ci = list(map(int,input().split()))
        allsum += ci*c[bi] - bi*c[bi]
        c[ci] = c[ci] + c[bi]
        c[bi] = 0
        ans.append(allsum)
    for i in ans:
        print(i)    
main()