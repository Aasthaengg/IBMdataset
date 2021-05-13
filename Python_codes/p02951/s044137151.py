a, b, c = map(int, input().split())

# aは容量、b,cは入っている水の量
cap = a - b
print(c - cap) if (c - cap) >= 0 else print('0')