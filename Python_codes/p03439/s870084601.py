N = int(input())
low = 0
high = N - 1
t = (low + high) // 2
flag = 0
print(0)
resl = input()
print(N-1)
resr = input()
if resl == "Vacant" or resr == "Vacant":
    flag = 1

while(flag == 0):
    print(t)
    inp = input()
    if inp == "Vacant":
        break
    if (high-t) % 2 == 0 and inp != resr:
        low = t
        resl = inp
    elif (high-t) % 2 == 1 and inp == resr:
        low = t
        resl = inp
    elif (t-low) % 2 == 0 and inp != resl:
        high = t
        resr = inp
    else:
        high = t
        resr = inp
    t = (low + high) // 2

