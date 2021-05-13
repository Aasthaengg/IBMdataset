ans = set()
for q in range(int(input())):
    l, r = map(int, input().split())
    ans |= set(range(l, r + 1))
print(len(ans))