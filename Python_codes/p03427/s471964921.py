N = input()
c = N[0]
K = len(N)

temp = int(c + "9"*(K-1))
temp_s = sum(int(a) for a in list(str(temp)))

if temp <= int(N):
    print(temp_s)
else:
    print(temp_s - 1)
