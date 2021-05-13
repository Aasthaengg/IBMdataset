N = int(input())
sX = input()

origin_count = sX.count('1')
one_r_count = origin_count -1
zero_r_count = origin_count +1

one_mod = 0
zero_mod =0
for b in sX:
    if one_r_count != 0:
        one_mod = (one_mod * 2 + int(b) )% one_r_count
    zero_mod = (zero_mod * 2  + int(b) )% zero_r_count

f = [0] * 220000
pop = [0]* 220000

for i in range(1,220000):
    pop[i] = pop[i//2] + i%2
    f[i] = f[i % pop[i]] + 1

onepow = [1] * 220000
zeropow = [1]* 220000

for i in range(1,220000):
    if one_r_count != 0:
        onepow[i] = onepow[i-1] * 2 % one_r_count
    zeropow[i] = zeropow[i-1] * 2 % zero_r_count

for i in range(1,N+1):
    if sX[i-1] == '1':
        if one_r_count != 0:
            Xi_n = one_mod - onepow[N-i]
            Xi_n %= one_r_count
            print(f[Xi_n]+1)
        else:
            print(0)
    else:
        Xi_n = zero_mod + zeropow[N-i]
        Xi_n %= zero_r_count
        print(f[Xi_n]+1)