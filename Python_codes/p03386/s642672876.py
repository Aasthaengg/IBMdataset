A,B,K = map(int, input().split())
if B - A + 1> 2*K:
    a = list(range(A, A+K))
    b = list(range(B-K+1,B+1))
    c = sorted(set(a+b))
    print(*c, sep="\n")
else:
    print(*range(A,B+1), sep="\n")