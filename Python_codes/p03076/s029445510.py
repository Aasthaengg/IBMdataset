l = [int(input()) for _ in range(5)]
m = [(x+9)//10*10 for x in l]
d = [x - y for (x, y) in zip(m, l)]
print(sum(m)-max(d))