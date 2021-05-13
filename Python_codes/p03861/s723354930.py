A, B, X = map(int, input().split())

P, r = divmod(A, X)
if r:
    P += 1

Q, r = divmod(B, X)

#print(P, Q)
print(max(0, Q-P+1))