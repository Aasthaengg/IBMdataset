from statistics import mean

N = input()
a = [int(x) for x in input().split(' ')]

avg = mean(a)

tmp = []
result = []
for x in a:
    tmp.append(abs(x - avg))
    
tmp_min = min(tmp)
for i in range(len(tmp)):
    if tmp[i] == tmp_min:
        print(i)
        break