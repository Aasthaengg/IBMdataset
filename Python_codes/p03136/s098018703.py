N = int(input())
Ls = sorted(map(int, input().split()))
if Ls[-1] < sum(Ls) - Ls[-1]:
    print('Yes')
else:
    print('No')