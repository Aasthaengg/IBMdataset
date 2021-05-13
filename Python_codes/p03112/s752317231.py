import bisect
import itertools
import sys

def main(args):
    
    A, B, Q = map(int,input().split())
    S = [0]*A
    T = [0]*B
    for i in range(A):
        S[i] = int(input())
    for i in range(B):
        T[i] = int(input())
    
    S = [-10**18] + S + [10**18]
    T = [-10**18] + T +[10**18]
    
    def solve(j, t, start):
        jinja_l = S[j-1]
        jinja_r = S[j]
        tera_l = T[t-1]
        tera_r = T[t]
        jinja = [jinja_l, jinja_r]
        tera = [tera_l ,tera_r]
        
        ans = float('inf')
        for u,v in list(itertools.product(jinja, tera)):
            ans = min(ans, abs(start-u)+abs(v-u))
            ans = min(ans, abs(v-start)+abs(v-u))
        
        return ans
    
    for i in range(Q):
        x = int(input())
        ans = solve(bisect.bisect_left(S, x), bisect.bisect_left(T ,x), x)
        print(ans)
        
if __name__ == '__main__':
    main(sys.argv[1:])