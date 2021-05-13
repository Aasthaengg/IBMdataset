from collections import Counter

N = int(input())

S_list = []

for i in range(N):
    str = input()
    S_list.append(str)

print(len(list(Counter(S_list))))
