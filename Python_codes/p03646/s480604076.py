k = int(input())
ans = [k//50] * 50
for i in range(50):
    ans[i] += i + 1
for i in range(50 - (k % 50)):
    ans[i] -= 1

print(50)
for item in ans:
    print(item, end=" ")