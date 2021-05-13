instr = input()
instrSp = instr.split()

a = int(instrSp[0])
b = int(instrSp[1])
c = int(instrSp[2])

cnt = 0
for i in range(a, b + 1):
    if c % i == 0:
        cnt += 1
print(cnt)

