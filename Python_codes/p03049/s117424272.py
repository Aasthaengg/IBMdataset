s = [input() for _ in range(int(input()))]
a = b = ab = ans = 0
for si in s:
    for j in range(len(si)-1):
        if si[j] == "A" and si[j+1] == "B":
            ans += 1
    if si[0] == "B" and si[-1] == "A":
        ab += 1
    elif si[0] == "B":
        b += 1
    elif si[-1] == "A":
        a += 1
print(ans + max(ab-1, 0)) if a == b == 0 else print(ans + ab + min(a, b))