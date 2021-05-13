l = list(map(int,input().split()))

if sum(l[:2]) == sum(l[2:]): print('Balanced')
elif sum(l[:2]) > sum(l[2:]): print('Left')
else: print('Right')