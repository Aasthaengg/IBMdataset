A, B = input().split()

ans_list =[]

for i in range(int(A), int(B)+1):
    i_reversed = int(str(i)[::-1])
    if i_reversed == i:
        ans_list.append(i)
    i += 1
        
print(len(ans_list))