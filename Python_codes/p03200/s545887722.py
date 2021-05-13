S=list(input())
total_count=0
b_count=0

for n in range(len(S)):
    if S[n]=='B':
        b_count+=1
    if S[n]=='W':
        total_count+=b_count
print(total_count)
