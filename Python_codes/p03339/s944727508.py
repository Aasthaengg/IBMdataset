n = int(input())
s = input()

e_list = [0] * n
for i in range(n - 2, -1, -1):
    e_list[i] = (1 if s[i + 1] == "E" else 0) + e_list[i + 1]

w_list = [0] * n
for i in range(1, n):
    w_list[i] = (1 if s[i - 1] == "W" else 0) + w_list[i - 1]

print(min([e + w for e, w in zip(e_list, w_list)]))