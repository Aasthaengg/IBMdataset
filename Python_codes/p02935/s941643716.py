N = int(input())
v = [int(v) for v in input().split()]

v_sorted = sorted(v)

new_list = []
for i in range(len(v)):
    if i == 0 or i == 1:
        new_list.append(v_sorted[i] / 2**(len(v)-1))
    else:
        new_list.append(v_sorted[i] / 2 ** (len(v)-i))
    
print(sum(new_list))