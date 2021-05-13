from collections import defaultdict

S = input()
T = input()

s_dic = defaultdict(list)
t_dic = defaultdict(list)


for i, ch in enumerate(S):
    s_dic[ch].append(i)

for i, ch in enumerate(T):
    t_dic[ch].append(i)

lis_s = list(s_dic.values())
lis_t = list(t_dic.values())

for i in range(len(lis_s)):
    if lis_s[i] != lis_t[i]:
        print("No")
        exit()
print("Yes") 