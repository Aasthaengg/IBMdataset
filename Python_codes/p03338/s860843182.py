N = int(input())
S = input()
chars = list("abcdefghijklmnopqrstuvwxyz")
ans_lst = []
for cut in range(1, N):
    left = S[:cut]
    right = S[cut:]
    count = 0
    for char in chars:
        if char in left and char in right:
            count += 1
    ans_lst.append(count)
print(max(ans_lst))