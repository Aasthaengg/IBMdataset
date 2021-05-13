n = int(input())
s = input()

ans = s.count("E")

tmp = ans

for i in s:
    tmp += (-1 if i == "E" else 1)
    ans = min(ans, tmp)

print(ans)
