# https://atcoder.jp/contests/agc006/tasks/agc006_a

n = int(input())
s = input()
t = input()

string = s + t
ans = len(string)

for i in range(len(string)):
    for j in range(i, len(string)):
        sub = string[:i] + string[j:]
        if len(sub) >= n:
            if sub[:n] == s and sub[-n:] == t:
                ans = min(ans, len(sub))
print(ans)