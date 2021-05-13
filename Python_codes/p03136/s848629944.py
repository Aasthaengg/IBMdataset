n = int(input())
l = list(map(int, input().split()))

max_index = l.index(max(l))
cnt = 0
for i in range(len(l)):
    if not  i == max_index:
        cnt += l[i]
if cnt > l[max_index]:
    print("Yes")
else:
    print("No")