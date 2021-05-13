S = input()
cnt = 0

for i in range(len(S)):
    j = len(S) - i - 1
    if S[i] != S[j] and i < j:
        cnt += 1
        
print(cnt)