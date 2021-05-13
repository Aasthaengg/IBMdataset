lis = [int(input()) for _ in range(5)]
lis2 = [i % 10 for i in lis]

x = 0
a = 9
time = 0

for id,val in enumerate(lis2):
    if 0 < val < a:
        x = id
        a = val

for id2, val2 in enumerate(lis):
    if id2 == x:
        continue
    else:
        time += (-(-val2//10)) * 10

print(time+lis[x])
