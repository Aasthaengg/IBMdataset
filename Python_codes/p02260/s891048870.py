n = int(raw_input())

s = raw_input()

count = 0

num_list= s.split(" ")
for i in range(n):
    num_list[i] = int(num_list[i])

for i in range(n):
    minj = i
    for j in range(i, n):
        if num_list[j] < num_list[minj]:
            minj = j
    num_list[i], num_list[minj] = num_list[minj], num_list[i]
    if i != minj:
        count += 1

print " ".join([str(a) for a in num_list])
print count