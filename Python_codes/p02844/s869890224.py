n = int(input())
s = input()

counter = 0
for i in range(10):
    str_i = str(i)
    i_dig = s.find(str_i)
    if i_dig == -1:
        continue

    for j in range(10):
        str_j = str(j)
        j_dig = s.find(str_j, i_dig+1)
        if j_dig == -1:
            continue
        
        for k in range(10):
            str_k = str(k)
            k_dig = s.find(str_k, j_dig+1)
            if k_dig != -1:
                counter += 1

print(counter)