S = list(input())
sei = list('CODEFESTIVAL2016')
count = 0
for i in range(16):
    if S[i] != sei[i]:
        count += 1
print(count)