n = int(input())
a = list(map(int,input().split()))
count = 0
i_max = 0
for i in a:
    if i_max > i:
        count += i_max - i
    i_max = max(i_max,i)
print(count)