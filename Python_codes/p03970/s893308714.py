# Problem A - Signboard

# input process
S = input()

# initialization
teacher_data = "CODEFESTIVAL2016"
swap_count = 0

# count process
for i in range(len(S)):
    if not S[i]==teacher_data[i]:
        swap_count += 1

# output process
print(swap_count)
