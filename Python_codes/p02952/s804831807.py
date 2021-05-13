S = input()
slen = len(S)
S = int(S)
count = 0
for i in range(0,slen, 2):
    if ( i == slen-1):
        inv = 1 if i == 0 else 10 ** i
        count = count + (S-inv) + 1
        # print(i, (S-inv) + 1)
    else:
        count = count + 10 ** (i+1) - 10 ** (i)
        # print(i, 10 ** (i+1) - 1)
print(count)