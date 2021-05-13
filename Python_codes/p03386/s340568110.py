# input
A, B, K = map(int, input().split())

# check
if A + K > B:
    res = list(range(A, B + 1))
else:
    res = set(list(range(A, A + K)) + list(range(B, B - K, -1)))
    
for n in sorted(list(res)):
    print(n)