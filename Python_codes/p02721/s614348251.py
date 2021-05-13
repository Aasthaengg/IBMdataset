INF = 1 << 60

n, k, c = map(int, input().split())
s = input()

left = []
b = -INF
cnt1 = 0
for i in range(n):
    if cnt1 == k:
        break
    if s[i] == "x":
        continue
    if b + c < i:
        b = i
        cnt1 += 1
        left.append(i)

right = []
b2 = INF
cnt2 = 0
for i in reversed(range(n)):
    if cnt2 == k:
        break
    if s[i] == "x":
        continue   
    if b2 - c > i:
        b2 = i
        cnt2 += 1
        right.append(i)

right = right[::-1]

# print("right =", right)
# print("left =", left)
m = len(left)
ans = []
for i in range(m):
    if right[i] == left[i]:
        ans.append(right[i])
for i in ans:
    print(i + 1)