N = int(input())
S = input()
al = [0 for _ in range(26)]
for i in range(N):
    al[ord(S[i])-97] += 1
count = 1
for j in range(26):
    count *= al[j]+1
    count %= 10**9+7
print((count-1)%(10**9+7))