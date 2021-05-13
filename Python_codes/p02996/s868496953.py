#直感を証明できなかった

n = int(input())
l = []
for i in range(n):
    a,b = map(int, input().split())
    l.append((b, a)) #終了時間、工数
l = sorted(l) #終了時間が速い順に並べる

def check(l):
    t = 0 #現時刻
    for end, worktime in l:
        t += worktime
        if t > end:
            return 'No'
            break
            
    return 'Yes'
print(check(l))