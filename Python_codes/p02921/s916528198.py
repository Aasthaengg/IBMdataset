s = input()
t = input()
c = sum([ 1 for i,j in zip(s,t) if i == j])
print(c)