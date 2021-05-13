K ,A, B = map(int,input().split())

if B - A <= 2 or K <= A: #交換しても増やせないorお金をビスケットに交換できない
    ans = K + 1
else:
    n = K - (A + 1)
    n_loop =  n // 2
    n_tataku = n % 2
    ans = B + n_loop * (B-A) + n_tataku
print(ans)
