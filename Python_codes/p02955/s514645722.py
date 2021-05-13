import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

candidates = []
sumA = sum(A)

i = 1
while i <= math.sqrt(sumA):
    if sumA % i == 0:
        candidates.append(i)
        candidates.append(int(sumA / i))
    i += 1
    
candidates = sorted(candidates, reverse = True)
end = 0
# candidates loop
for i in range(len(candidates)):
    if end:
        break
    # A loop
    T = [0] * len(A)
    for j in range(len(A)):
        T[j] = A[j] % candidates[i]
    T = sorted(T)
    left = sum(T)
    right = 0
    need = max(left, right)
    for l in range(len(T) - 1, -1, -1):
        left -= T[l]
        right += candidates[i] - T[l]
        need = min(need, max(left, right))
    if need <= K:
        print(candidates[i])
        end = 1