# A - Shrinking

s = input()
N = len(s)
ans = 1000

for i in range(N):
    count = count_max = 0
    for j in range(1,N+1):
        if s[i]==s[N-j]:
            count = 0
        else:
            count += 1
        count_max = max(count, count_max)
    ans = min(count_max, ans)

print(ans)