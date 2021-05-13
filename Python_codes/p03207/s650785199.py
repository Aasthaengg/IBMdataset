n = int(input())
p_l = []
for _ in range(n):
    p_l.append(int(input()))
    
# print(p_l)
# print(sum(p_l))

p_l_s = sorted(p_l, reverse=True)
# print(p_l_s)
p_l_s[0] = int(p_l_s[0] / 2)
# print(p_l_s)

print(sum(p_l_s))