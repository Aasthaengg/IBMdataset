S = input()

B_index_sum = 0
for i in range(len(S)):
    if S[i] == "B":
        B_index_sum += i+1

B_count = S.count("B")
destination_B_index_sum = (len(S)*B_count) - sum(range(B_count))

print(max(0, destination_B_index_sum - B_index_sum))