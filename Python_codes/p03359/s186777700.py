

endday = [31] * 13
endday[2] = 28
for i in [4,6,9,11]:
    endday[i] = 30

a, b = map(int, input().split())

res = 0
done = False
for m in range(1, 13):
    if done:
        break
    for d in range(1, endday[m] + 1):
        if m == d:
            res += 1
        if m == a and d == b:
            done = True
            break

print(res)
