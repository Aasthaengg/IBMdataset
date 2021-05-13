n = int(input())
s = ["".join(sorted(list(input()))) for _ in range(n)]
s.sort()
ans=0
pairs=1
for i in range(n-1):

    if s[i]==s[i+1]:
        pairs += 1
    else:      
        ans += pairs*(pairs-1)/2
        pairs =1
if pairs != 1:
    ans += pairs*(pairs-1)/2
    pairs =1
print(int(ans))