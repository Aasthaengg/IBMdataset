_, *a = open(0)
print(sum(len(set(i))-1 for i in zip(*a)))