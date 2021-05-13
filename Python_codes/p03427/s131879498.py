N = input()
res = 9*(len(N)-1)+int(N[0])-1
if str(int(N)+1)[0] != N[0]:
    res += 1
if len(N) == 1:
    res = N
print(res)