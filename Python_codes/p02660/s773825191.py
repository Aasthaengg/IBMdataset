N = int(input())


hash = {}
end = int(N ** (1/2))
for i in range(2, end + 1):
    while N % i == 0:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
        N = N // i
if N != 1:
        if N in hash:
            hash[N] += 1
        else:
            hash[N] = 1

if len(hash.keys()) == 0 and N != 1:
    print(1)
    exit()


count = 0
trans = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

res = 0
for i in hash.values():
    for j in range(len(trans)):
        if i > trans[j]:
            continue
        elif i == trans[j]:
            res += (j + 1)
            break
        else:
            res += j
            break



print(res)