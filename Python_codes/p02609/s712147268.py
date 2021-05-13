n = int(input())
x = input()
x_popcnt = x.count('1')
one_popcnt = x_popcnt - 1
zero_popcnt = x_popcnt + 1

one_mod = 0
zero_mod = 0
for b in x:
    if one_popcnt != 0:
        one_mod = (one_mod*2 + int(b)) % one_popcnt
    zero_mod = (zero_mod*2 + int(b)) % zero_popcnt

f = [0]*220000
popcnt = [0]*220000
for i in range(1, 220000):
    popcnt[i] = popcnt[i//2] + i % 2
    f[i] = f[i % popcnt[i]] + 1

onepow2 = [1]*220000
if one_popcnt != 0:
    for i in range(1, 220000):
        onepow2[i] = 2*onepow2[i-1] % one_popcnt
zeropow2 = [1]*220000
for i in range(1, 220000):
    zeropow2[i] = 2*zeropow2[i-1] % zero_popcnt
for i in range(n-1, -1, -1):
    if x[n-1-i] == '1':
        if one_popcnt != 0:
            nxt = one_mod
            nxt -= onepow2[i]
            nxt %= one_popcnt
            print(f[nxt]+1)
        else:
            print(0)
    if x[n-1-i] == '0':
        nxt = zero_mod
        nxt += zeropow2[i]
        nxt %= zero_popcnt
        print(f[nxt]+1)
