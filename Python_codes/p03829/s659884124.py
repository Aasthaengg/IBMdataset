import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    n , a, b = f()
    x = f()
    dis = [x[i+1] - x[i] for i in range(n-1)]


    ans = 0
    for i in dis:
        if i*a <= b:
            ans += i * a
        else:
            ans += b
    
    print(ans)


solve()
