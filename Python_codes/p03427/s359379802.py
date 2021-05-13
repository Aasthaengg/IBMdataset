N = input()
ndig = len(N)
ans1 = N[0] + "9" * (ndig - 1)
ans2 = str(int(N[0]) - 1) + "9" * (ndig - 1)
if int(ans1) <= int(N):
    print(sum(int(d) for d in ans1))
else:
    print(sum(int(d) for d in ans2))