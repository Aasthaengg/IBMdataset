A, B, C = map(int, input().split())
num = [A, B, C]
cnt =0

for i in range(2):
    multi = (max(num)-min(num))//2
    num[num.index(min(num))] += 2*multi
    cnt += multi

if len([i for i in num if i==max(num)]) ==1:
    cnt += 1
elif len([i for i in num if i==max(num)]) ==2:
    cnt += 2
print(cnt)

