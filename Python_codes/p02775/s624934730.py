n = list(map(int, list(input())))
n.reverse()
n.append(0)
ans = 0

for i in range(len(n)):
    # d <= 4 -> and += d
    # d == 5 -> next d <= 4 ans += d else ans += d next digit += 1
    # d >= 6 -> ans += 10 - d next digit += 1
    if n[i] <= 4:
        ans += n[i]
    elif n[i] == 5:
        if n[i + 1] <= 4:
            ans += n[i] 
        else:
            ans += n[i]
            n[i + 1] += 1
    else:
        ans += 10 - n[i]
        n[i + 1] += 1
print(ans)
