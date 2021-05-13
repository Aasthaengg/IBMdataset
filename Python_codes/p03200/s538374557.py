S = input()

w_list = [0]
ans=0
for i in range(len(S)):
    if S[i]=='W':
        w_list.append(i+1)

for i in range(1,len(w_list)):
    ans += w_list[i]-i
    
print(ans)