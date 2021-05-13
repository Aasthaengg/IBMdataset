n = int(raw_input())
if n > 1:
    s = map(int, raw_input().split())
else:
    s = int(raw_input())
    
q = int(raw_input())
if q > 1:
    t = map(int, raw_input().split())
else:
    t = int(raw_input())

count = 0
for i in range(q):
    try:
        a = s.index(t[i])
        count += 1
    except:
        pass

print count