N = int(input())
a = map(int, input().split())

other = mult_2 = mult_4 = 0
for t in a:
    if t % 4 == 0:
        mult_4 += 1
    elif t % 2 == 0:
        mult_2 += 1
    else:
        other += 1

if other - 1 + (1 if mult_2 > 0 else 0) <= mult_4:
    print("Yes")
else:
    print("No")
