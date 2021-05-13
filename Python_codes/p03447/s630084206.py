x = int(input())
a = int(input())
b = int(input())
wallet = x - a
d_count = wallet // b
ans = wallet - b * d_count
print(ans)
