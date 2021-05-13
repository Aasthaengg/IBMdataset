N,K = (int(x) for x in input().split())
S = list(input())
S[K-1] = S[K-1].swapcase()
print(''.join(S))