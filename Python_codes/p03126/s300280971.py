N,M = map(int,list(input().split()))
i_list = [0]*M
for i in range(N):
    s = list(input().split())
    for j in range(int(s[0])):
        i_list[int(s[j+1])-1] += 1
     #   print(i_list)
counter = 0
for i in range(M):
    if i_list[i] == N:
        counter += 1   
    
print(counter)
