N, M, D = [int(_) for _ in input().split()]
#A[i]∈[0,n)で考察したときの解と一致
#x∈[0,N-D) and D<N ⇒ x+D∈[0,N)
#x∈[D,N) and D<N⇒ x-D∈[0,N)
if D == 0:
    ans = (M - 1) / N
elif D < N - D:
    ans = (2 * (N - 2 * D) + 2 * D) * (M - 1) / N / N
elif D < N:
    ans = (2 * N - 2 * D) * (M - 1) / N / N
else:
    ans = 0
print(ans)
