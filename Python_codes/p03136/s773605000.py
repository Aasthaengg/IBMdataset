N = int(input())
L = [int(i) for i in input().split()]
L.sort()

M = L.pop()
if M < sum(L):
    print('Yes')
else:
    print('No')