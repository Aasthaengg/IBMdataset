N = int(input())

ans_rev = "" if N else "0"
while N:
    if N % 2 == 1:
        ans_rev += '1'
        N -= 1
    else:
        ans_rev += '0'
    N //= (-2)

print(ans_rev[::-1])