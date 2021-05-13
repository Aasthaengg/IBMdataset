N = int(input())

ans = 0
word = {}
for i in range(N):
    S_word = sorted(input())
    key = "".join(S_word) 
    if key in word:
       word[key] += 1
       ans += word[key]
    else:
        word[key] = 0

print(ans)