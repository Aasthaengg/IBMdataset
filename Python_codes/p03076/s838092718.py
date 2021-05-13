l = [int(input()) for _ in range(5)]
m = [(x+9)//10*10 for x in l]
s = sum(m)
print(min([s-m[i]+l[i] for i in range(5)]))