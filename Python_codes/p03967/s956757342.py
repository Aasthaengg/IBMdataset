N = input()
ans = 0
for i in range(len(N)):
    if i%2 == 0:
        if N[i] =="p":
            ans += -1
    else:
        if N[i] =="g":
            ans += 1
print(ans)