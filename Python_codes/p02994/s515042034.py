import sys
N, L = map(int, input().split())
tastes = [ L+x for x in range(N) ] 

if 0 in tastes:
    print(sum(tastes))
    sys.exit(0)
    

if L<0:
    absmin = max(tastes)
    print(sum(tastes)-absmin)
elif L>0:
    absmin = min(tastes)
    print(sum(tastes)-absmin)
