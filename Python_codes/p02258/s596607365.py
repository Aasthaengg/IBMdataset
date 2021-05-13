n = int(input())
mi = int(input())
diff = -9999999999999999
for i in range(n-1):
    now = int(input())
    diff = max(diff, now-mi)
    mi = min(mi, now)
print(diff)