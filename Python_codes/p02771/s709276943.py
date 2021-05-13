S = input().split()
for i in range(-1, 2):
    if S[i-1] == S[i] and S[i] != S[i+1]:
        print("Yes")
        exit()
else:
    print("No")