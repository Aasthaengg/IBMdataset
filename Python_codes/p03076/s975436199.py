from math import ceil

t = [int(input()) for _ in range(5)]
t.sort(key=lambda x: ((x%10)-1)%10+1)
print(t[0] + sum(map(lambda x: ceil(x/10)*10, t[1:])))
