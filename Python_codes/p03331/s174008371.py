# A - Digits Sum

N = input()
N_int = int(N)
mylist = ['10','100','1000','10000','100000']
ans = 0

if N in mylist:
    ans = 10
else:
    for i in range(len(N)):
        ans += (N_int % 10)
        N_int = N_int // 10

print(ans)