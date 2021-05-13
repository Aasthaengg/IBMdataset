N = int(input())
S = input()
flag = True if N % 2==0 else False

for i in range(N//2):
    if S[i] != S[N//2 + i]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
