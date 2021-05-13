N = int(input())
numbers = [int(i)-1 for i in input().split()]

need_fix_index = []

for i, v in enumerate(numbers):
    if i == v:
        need_fix_index.append(i)
        
cnt = 0

while need_fix_index:
    cnt += 1
    v = need_fix_index.pop(0)
    if len(need_fix_index) == 0:
        break
    if abs(need_fix_index[0]-v) == 1:
        del need_fix_index[0]
    
print(cnt)