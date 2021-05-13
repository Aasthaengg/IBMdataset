N = input()
S = [int(n) for n in N]
if sum(S) % 9 == 0:
    print("Yes")
else:
    print("No")