S = input()
N = len(S)
reverse = S[::-1]
first = S[:(N - 1) // 2]
second = S[(N + 1) // 2:]

if S == reverse and first == second:
    print("Yes")
else:
    print("No")
