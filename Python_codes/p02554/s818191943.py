N = int(input())

p_all = 10 ** N
p_no0 = 9 ** N
p_no9 = 9 ** N
p_no09 = 8 ** N

ans = (p_all - p_no0 - p_no9 + p_no09) % (10 ** 9 + 7)

print(ans)