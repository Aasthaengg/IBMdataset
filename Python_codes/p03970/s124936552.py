A = list("CODEFESTIVAL2016")
S = list(input())
count = 0
for i, j in zip(A, S):
    if i != j:
        count += 1
print(count)
