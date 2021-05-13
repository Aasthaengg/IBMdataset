N = input()
cnt = 0
for i in range(len(N)):
    if int(N[i]) == 2:
        cnt += 1
print(cnt)