L = list(map(int, input().split()))
if sum(L[:2]) == sum(L[2:]):
    print('Balanced' , flush=True)
elif sum(L[:2]) > sum(L[2:]):
    print('Left' , flush=True)
else:
    print('Right' , flush=True)

