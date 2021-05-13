N = list(range(1, int(input())+1))

cnt = 0
for n in N:
    cnt += n%2!=0
    
print(cnt/len(N))