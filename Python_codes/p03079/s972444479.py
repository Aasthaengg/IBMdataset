inp = [int(n) for n in input().split(" ")]
res = inp[0] == inp[1] and inp[0] == inp[2] and 1 <= inp[0] <= 100

if res:
    print("Yes")
else:
    print("No")