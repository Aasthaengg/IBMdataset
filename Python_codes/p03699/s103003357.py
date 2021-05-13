N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
total = sum(S)
T = [s for s in S if s % 10 != 0]
if total % 10 != 0:
    print(total)
elif len(T) > 0:
    print(total - T[0])
else:
    print(0)