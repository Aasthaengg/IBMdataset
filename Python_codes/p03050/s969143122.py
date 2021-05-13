N = int(input())


ans = 0

for i in range(1, 1000000):
    if N <= i:
        break
    # if (N-i) == i:
    #    break

    if (N - i) % i == 0:
        a = (N-i) // i
        if a <= i:
            break
        ans += a
        #print(i, (N-i) // i)

print(ans)
