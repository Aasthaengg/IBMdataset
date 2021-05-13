N, A, B = map(int, input().split())
H = [0] * N
for i in range(N):
    H[i] = int(input())

sorted_H = sorted(H, reverse=True)

def is_enough(num):
    cnt = 0
    for x in range(N):
        if sorted_H[x] - num * B > 0:
            cnt += (sorted_H[x] - num * B) // (A - B)
            if (sorted_H[x] - num * B) % (A - B) != 0:
                cnt += 1
        else:
            break
    return cnt <= num

limit = (sorted_H[0] // B) + 1

i = 0
j = limit
while True:
    k = (j + i) // 2
    if is_enough(k):
        if i + 1 == k:
            print(k)
            break
        j = k
    else:
        if k + 1 == j:
            print(k + 1)
            break
        i = k
