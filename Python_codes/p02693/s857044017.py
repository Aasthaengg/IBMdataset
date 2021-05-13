K = int(input())
A, B = map(int, input().split())

can_K_times = False
if (A % K) == 0 or (B % K) == 0:
    can_K_times = True
elif (A // K) != (B // K):
    can_K_times = True


if can_K_times:
    print("OK")
else:
    print("NG")