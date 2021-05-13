import sys
input = sys.stdin.readline

n,m=map(int,input().split())
C = [list(map(int,input().split())) for _ in range(m)]

for i in range(1000):
    S = str(i)
    if len(S)==n:
        for s,c in C:
            s-=1
            if S[s]==str(c):
                True
            else:
                break
        else:
            print(i)
            sys.exit()
print(-1)

