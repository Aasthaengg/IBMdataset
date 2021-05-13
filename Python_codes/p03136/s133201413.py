N = int(input())
L = list(map(int, input().split()))

M = max(L)
S = sum(L) - M

print('Yes' if M < S else 'No')