N = int(input())
S = input()

chars = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz"
chars = chars.upper()
dic = {chars[i]: chars[i+N] for i in range(26)}
ans = ""
for i in range(len(S)):
    ans += dic[S[i]]

print(ans)