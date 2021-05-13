x = input()
cnt = 0
for i in range(4):
    cnt += 1 if x[i]=='2' else 0
print(cnt)