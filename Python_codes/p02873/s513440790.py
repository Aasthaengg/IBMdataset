S = input()
n = len(S)
shift_max = [0]*(n+1)

big_run = 0
for i in range(n):
    if S[i] == '<':
        big_run += 1
    else:
        big_run = 0
    shift_max[i+1] = big_run
small_run = 0
for i in reversed(range(n)):
    if S[i] == '>':
        small_run += 1
    else:
        small_run = 0
    shift_max[i] = max(shift_max[i],small_run)

print(sum(shift_max))

