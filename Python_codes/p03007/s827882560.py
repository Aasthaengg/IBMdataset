N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

P = [x for x in A if x >= 0]
M = [x for x in A if x < 0]

if not len(P):
    P.append(A[0])
    M = M[1:]
elif not len(M):
    P.pop()
    M.append(A[-1])

print(sum(P) - sum(M))
# -
x = M[0]
for i in range(1, len(P)):
    print(x, P[i])
    x -= P[i]

# +
y = P[0]
for i in range(1, len(M)):
    print(y, M[i])
    y -= M[i]
print(y, x)
