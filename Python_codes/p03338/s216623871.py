N = int(input())
S = input()

ans = 0
for i in range(N - 1):
    a = S[:i + 1]
    b = S[i + 1:]
    count = 0
    for j in range(97, 123):
        if chr(j) in a and chr(j) in b:
            count += 1
    if count > ans:
        ans = count
print(ans)
