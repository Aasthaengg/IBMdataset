S=input()
S=S[::-1]
B_index=[i for i, x in enumerate(S) if x == 'B']
for i in range(len(B_index)):
    B_index[i]=B_index[i]-i
print(sum(B_index))