d = list(map(int,open(0)))
d.sort(key=lambda x:(x-1)%10, reverse=True)
print(sum((x+9)//10*10 for x in d[:-1]) + d[-1])
