A,B,K = map(int, input().split())

if B-A+1<= 2*K:
    print(*range(A,B+1), sep="\n")
else:
    a = list(range(A,A+K))
    b = list(range(B-K+1,B+1))
    C = sorted(set(a+b))
    print(*C, sep="\n")