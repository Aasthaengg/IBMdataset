s_dict = dict()
n = int(input())
for _ in range(n):
    s = input()
    if not s in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1
n = int(input())
for _ in range(n):
    s = input()
    if s in s_dict:
        s_dict[s] -= 1
print(max(max(s_dict.values()), 0))