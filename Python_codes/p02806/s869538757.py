n = int(input())
li_a = list()
for i in range(n):
    li_a.append(input().split())

s = input()
sum_t =0
for i in range(n):
    if li_a[i][0]==s:
        x = i+1
        break
for i in range(x,n):
    sum_t += int(li_a[i][1])
print(sum_t)