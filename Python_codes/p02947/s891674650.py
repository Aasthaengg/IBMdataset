N = int(input())

S = []
for i in range(N):
    s = input()
    s = list(s)
    s = sorted(s)
    S.append(s)

S = sorted(S)
count = 1
ans = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        count += 1
    else:
        ans += (count * (count-1)) // 2
        count = 1
ans += (count * (count-1)) // 2
        
print(ans)