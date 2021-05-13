#!/usr/bin/env python

# Initially, all cards face up.
# Given that N,M >= 0.
# Let N <= M.
# Ultimately:
#   if N,M==1:      singular card will flip.
#   elif N==1:      interior cards will flip (interior to line).
#   else N,M > 1:   interior cards will flip (interior to area).

# Fetching input
N,M = map(int,input().split())

# Ensuring N <= M
if N > M:
    M,N = N,M

# Requires N <= M:
def numflips(N,M):
    if N==0: return 0
    if N==1:
        if M==1: return 1
        return (M-2)
    return (N-2)*(M-2)

ans = numflips(N,M)
print(ans)