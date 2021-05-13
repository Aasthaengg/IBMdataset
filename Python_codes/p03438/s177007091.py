n = int(input())
a_ls = list(map(int, input().split()))
b_ls = list(map(int, input().split()))
times_add = 0
diff_to_pad = 0
for i in range(n):
    diff = b_ls[i] - a_ls[i]
    if diff > 0:
        times_add += -(-diff//2) 
        if diff % 2 == 1:
            diff_to_pad += 1
    elif diff < 0:
        diff_to_pad += -diff
if diff_to_pad > times_add:
    res = 'No'
else:
    res = 'Yes'
print(res)

