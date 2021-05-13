n=int(input())
L=list(map(int, input().split()))
L.sort(reverse=True)
maxL=L.pop(0)
if maxL< sum(L):
    print('Yes')
else:
    print('No')
