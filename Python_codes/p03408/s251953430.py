s ={}
n = int(input())
for _ in range(n):
    word = input()
    s[word] = s.get(word, 0)+1
m = int(input())
for _ in range(m):
    word = input()
    s[word] = s.get(word, 0)-1

ans = max(max(s[i],0) for i in s)
print(ans)
