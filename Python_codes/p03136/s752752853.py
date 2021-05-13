N = int(input())
L = list(map(int,input().split()))
maxL = max(L)
sumL = sum(L) - maxL
print('Yes' if maxL < sumL else 'No')