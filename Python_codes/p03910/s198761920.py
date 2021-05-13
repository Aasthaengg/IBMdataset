n = int(input())
cnt = 1
while cnt*(cnt+1)//2 < n:
    cnt+=1
if cnt*(cnt+1)//2 == n:
    for i in range(cnt):
        print(i+1)
else:
    bad = -1
    total = cnt*(cnt+1)//2
    for i in range(1, cnt+1):
        if total-i == n:
            bad = i
            break
    for i in range(1, cnt+1):
        if i == bad:
            continue
        print(i)
