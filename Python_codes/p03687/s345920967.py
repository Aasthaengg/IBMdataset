S = input()
alphabet = [[-1] for a in range(26)]
for n,c in enumerate(S):
    s = ord(c) - 97
    alphabet[s].append(n)

ans = float("inf")
for A in alphabet:
    A.append(len(S))
    cur = max([abs(A[l] - A[l+1]) for l in range(len(A)-1)])
    ans = min(cur,ans)
print(max(ans -1 , 0))