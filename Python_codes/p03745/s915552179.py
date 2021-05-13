from operator import lt, gt, le, ge
def get_monotonic_section(A, start=0, operator=lt):
    a0 = A[start]
    for i in range(start+1, len(A)):
        a = A[i]
        if not operator(a0, a):
            return i
        a0 = a
    return len(A)

n, *A = map(int, open(0).read().split())
c = t = 0
while t < n:
    t1 = get_monotonic_section(A, start=t, operator=le)
    t2 = get_monotonic_section(A, start=t, operator=ge)
    t = max(t1, t2)
    c += 1
print(c)