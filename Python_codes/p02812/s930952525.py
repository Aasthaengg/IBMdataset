N = int(input())
S = input()

a_lst = ([i for i, x in enumerate(S) if x == 'A'])
count = 0
for j in a_lst:
    if len(S) >= j + 3:
        if S[j+1] == 'B' and S[j+2] == 'C':
            count += 1
print(count)