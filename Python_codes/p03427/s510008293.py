n = int(input())
n_str = str(n)
ans = int(n_str[0])
if n_str[1:].count('9') != len(n_str) - 1:
    ans -= 1
ans += int(len(n_str[1:])) * 9
print(ans)
