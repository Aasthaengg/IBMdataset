N, K = list(map(int, input().split()))
S = input()

T = [s for s in S]
T[K - 1] = T[K - 1].lower()
print("".join(T)) 