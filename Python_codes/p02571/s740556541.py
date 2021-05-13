S = list(input())
T = list(input())
defolt = 1000
for i in range(len(S)-len(T)+1):
    ans = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            ans += 1
    defolt = min(defolt,ans)
print(defolt)