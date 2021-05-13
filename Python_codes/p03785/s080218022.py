n, c, k = map(int, input().split())
t = []    
for _ in range(n):
    t.append(int(input()))
t.sort()
first = t[0]
wait = 0
need = 1
for i in t:
    wait += 1
    if first + k < i or wait > c:
        need += 1
        wait = 1
        first = i
        continue
print(need)