A = input()
import collections
a_frq_dict = collections.Counter(A)

n_all = len(A) * (len(A)-1) * 0.5 + 1
n_duplication = 0
for frq in a_frq_dict.values():
    n_duplication += frq * (frq-1) * 0.5

print(int(n_all - n_duplication))
# print(n_all, n_duplication)

