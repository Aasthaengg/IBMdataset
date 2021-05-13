x = int(input())
'''
t =  1, 2, 3, 4, 5, 6,...
d+ = 1, 3, 6,10,15,21,...
x = 11のとき、
t = 5,d+ = 15より、t = 4で一回休みすればいい
-> 行き過ぎたら一回休み
'''
i = 0
d = 0
while True:
    i += 1
    d += i
    if x <= d:
        ans = i
        break
print(ans)