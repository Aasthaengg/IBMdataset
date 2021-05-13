s  = input()
se = set(s)

l = [max([len(j) for j in s.split(i)])for i in se]
print(min(l))