def successive_subtraction(N, A, i=1, l=[]):
    mx = max(A)
    mn = min(A)
    if i == N - 1:
        print(mx - mn)
        return l
    l.append((mn, mx))
    A.remove(mn)
    A.remove(mx)
    A.append(mn - mx)
    return successive_subtraction(N, A, i + 1, l)

N = int(input())
A = [int(e) for e in input().split()]
A.sort()
l = []
for i in range(N - 2):
    (a, b, c) = (A[0], A[1], A[-1])
    if b < 0:
        l.append((c, a))
        A[-1] = c - a
    else:
        l.append((a, b))
        A[1] = a - b
    A.pop(0)
print(A[1] - A[0])
l.append((A[1], A[0]))
for v in l:
    print(v[0], v[1])