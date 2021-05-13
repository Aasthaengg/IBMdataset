N, K = map(int, input().split())
S = input()
 
happiness = 0
 
for word in S.split("L"):
    happiness += max(0, len(word) - 1)
for word in S.split("R"):
    happiness += max(0, len(word) - 1)
 
res = happiness + 2 * K
print(min(res, N-1))