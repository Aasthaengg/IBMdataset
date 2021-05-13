n = int(input())
a_str = input()
b_str = input()
c_str = input()

ans = 0
for a, b, c in zip(a_str, b_str, c_str):
    if a == b == c:
        continue
    elif a == b or b == c or c == a:
        ans += 1
    else:
        ans += 2
print(ans)