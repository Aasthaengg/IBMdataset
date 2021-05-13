N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)
ln = L.pop(0)
if ln < sum(L):
    print('Yes')
else:
    print('No')