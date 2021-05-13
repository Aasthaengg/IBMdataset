n = int(input())
b = n.bit_length() - 1
ans = int('0b1'+'0'*b, 2)
print(ans)
