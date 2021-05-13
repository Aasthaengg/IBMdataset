from collections import Counter

S = input()
T = input()

counter_s = Counter(S)
counter_t = Counter(T)

# print(counter_s, counter_t)
s_value = sorted(counter_s.values())
t_value = sorted(counter_t.values())

# print(s_value, t_value)
if s_value == t_value:
    print("Yes")
else:
    print("No")
