N=int(input())
d=list(map(int,input().split()))
d_sort=sorted(d,reverse=False)
if d_sort[N//2]==d_sort[N//2-1]:
    print('0')
else:
    print(d_sort[N//2]-d_sort[N//2-1])