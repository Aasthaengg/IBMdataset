S = list(input())
N = len(S)
p = sum([1 if s == "p" else 0 for s in S])
print(N//2-p)