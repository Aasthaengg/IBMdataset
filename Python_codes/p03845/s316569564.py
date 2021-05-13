n = int(input())
tl = [0]+list(map(int, input().split()))
s = sum(tl)
m = int(input())
for _ in range(m):
    p, tx = map(int,input().split())
    print(s-tl[p]+tx)
