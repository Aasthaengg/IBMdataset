N = int(input())
S = input()
x = 0
maxi = 0
for char in S:
    if char == "I":
        x += 1
        maxi = max(maxi, x)
    else:
        x -= 1
print(maxi)