n  = int(input())
li = list(map(int,input().split()))
li.sort()
new_li = li[n:]
#print(new_li)
all_sum = 0
for i,n in enumerate(new_li):
    if i%2 == 0:
        all_sum += n
print(all_sum)