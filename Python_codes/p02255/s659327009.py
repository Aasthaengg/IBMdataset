num = int(raw_input())
line = raw_input()

item_str = line.strip().split(" ")
print " ".join(item_str)
A = map(int, item_str)

for i in range(1, num):
    v = A[i]
    j = i - 1
    for j in range(j, -1, -1):
        if A[j] > v:
            A[j+1] = A[j]
            j -= 1
        else:
            break
    A[j+1] = v
    str_A = map(str, A)
    print " ".join(str_A)