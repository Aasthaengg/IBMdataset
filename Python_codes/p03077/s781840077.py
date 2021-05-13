N = int(input())
Carry = []
for i in range(5):
    Carry.append(int(input()))
min_num = min(Carry)
if N < min_num:
    print(5)
elif min_num == 1:
    print((N//min_num)+4)
elif N % min_num == 0:
    print((N//min_num))
else:
    print((N//min_num)+5)