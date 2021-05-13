
S = input()

for i in range(len(S)):
    # 0オリジン[偶数]
    if i % 2 == 0:
        if S[i] not in ['R', 'U', 'D']:
            print("No")
            exit()
    else:
        if S[i] not in ['L', 'U', 'D']:
            print("No")
            exit()
print("Yes")