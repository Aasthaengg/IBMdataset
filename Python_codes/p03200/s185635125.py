S = input()
n = len(S)
l = [0 if S[i] == 'B' else 1 for i in range(n)]
cnt = 0
lenB = 1
for i in range(n-1):
    if l[i] == 0 and l[i+1] == 0: lenB += 1
    if l[i] == 0 and l[i+1] == 1:
        l[i+1] = 0
        cnt += lenB
print(cnt)