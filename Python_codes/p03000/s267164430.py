x = list(map(int, input().split()))[1]
l = list(map(int, input().split()))
m = [0]
for i in l:
    if i+m[-1] <= x:
        m.append(i+m[-1])
    else:
        break
print(len(m))