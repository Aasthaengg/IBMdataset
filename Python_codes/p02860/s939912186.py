N = int(input())
S = input()

tmp1 = S[:int(N / 2)]
tmp2 = S[int(N / 2):]

if tmp1 == tmp2:
    print("Yes")
else:
    print("No")
