N = int(input())
ans = 0
both = 0
start_B = 0
end_A = 0
for _ in range(N):
    s = input()
    ans += s.count("AB")
    isB = s.startswith("B")
    isA = s.endswith("A")
    if isA and isB:
        both += 1
    if isA:
        end_A += 1
    if isB:
        start_B += 1
ans += min(start_B, end_A)
if start_B == both and both == end_A and start_B != 0:
    ans = max(0, ans - 1)
print(ans)