A, B = map(int, input().split())
print(100, 100)
ans = [["."]*50 + ["#"]*50 for i in range(100)]


for a in range(A - 1):
    ans[2*(a // 25)][99 - 2*(a % 25)] = "."
for b in range(B - 1):
    ans[2*(b // 25)][2*(b % 25)] = "#"
for l in ans:
    print("".join(l))