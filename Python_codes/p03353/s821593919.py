#097_C
s = input()
k = int(input())
ans = set()

for i in range(1, min(k, len(s))+1):
    for j in range(len(s)-i+1):
        ans.add(s[j:(i+j)])

print(sorted(list(ans))[k-1])