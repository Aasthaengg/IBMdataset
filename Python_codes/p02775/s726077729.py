n = list(map(int, reversed(input()))) + [0]
ans = 0
for i in range(len(n)-1):
    if n[i] < 5:
        ans += n[i]
    elif n[i] == 5:
        if i != len(n) - 1 and n[i + 1] >= 5:
            n[i+1] += 1
            ans += 10 - n[i]
        else:
            ans += n[i]
    else:
        n[i+1] += 1
        ans += 10 - n[i]
if n[-1] > 0:
    ans += n[-1]
print(ans)