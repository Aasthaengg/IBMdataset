N = int(input())
S = input()
target = "ABC"
j = 0
count = 0
for i in range(N):
    if S[i] == target[0]:
        j = 0
    if S[i] == target[j]:
        j += 1
    else:
        j = 0
    if j == 3:
        count += 1
        j = 0
print(count)
        

