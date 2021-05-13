N = int(input())
S = input()
n = N // 2
T  = S[:n]
if S == T + T:
    print("Yes")
else:
    print("No")