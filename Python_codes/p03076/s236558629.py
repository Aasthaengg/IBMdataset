A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
times = [A,B,C,D,E]
remains = []
for t in times:
    remains.append(t%10)
last_item_i = -1
rmin = 1e8
for i in range(len(remains)):
    if remains[i] != 0 and remains[i] < rmin:
        rmin = remains[i]
        last_item_i = i
if last_item_i == -1:
    last_item_i = 0

ans = 0
for i in range(len(times)):
    if i != last_item_i:
        t = ((times[i] + 10 - 1)//10)*10
        ans += t

ans += times[last_item_i]

print(ans)
