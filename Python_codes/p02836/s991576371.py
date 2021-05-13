s = input()
l = list(s)
i = 0
j = len(l)-1
cnt = 0
while(i < j):
    if l[i] != l[j]:
        cnt = cnt+1

    i = i+1
    j = j-1

print(cnt)