n = int(input())
l = list(map(int,input().split()))
p = []
cnt = 0
for i in range(len(l)-1):
    if l[i+1] > l[i]:
        p.append(cnt)
        cnt = 0

    else:
        cnt = cnt+1

p.append(cnt)
p.sort()
print(p[-1])