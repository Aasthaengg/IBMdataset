N = int(input())
S = input()
tmp1 = int(N / 2)
tmp2 = S[0:tmp1]
tmp3 = S[tmp1:]
flag = False

if tmp2 == tmp3:
    print("Yes")
else:
    print("No")
