S = input()
A = 'Yes'
for i in range(len(S)):
    if i%2==0 and S[i] == 'L':
        A = 'No'
    elif i%2 == 1 and S[i] == 'R':
        A = 'No'
print(A)