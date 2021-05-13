S = input()
st_list =  []

for i in range(len(S)+1):
    if i==0:
        if S[i] == '<':
            st_list.append(i)
    elif i == (len(S)):
        if S[i-1] == '>':
            st_list.append(i)
    else:
        if (S[i-1] == '>') & (S[i] == '<'):
            st_list.append(i)
ans = [0] * (len(S)+1)
for i in st_list:
    j = i +1
    if j > (len(S)):
        pass
    else:
        while S[j-1] == '<':
            ans[j] = ans[j-1]+1
            j += 1
            if j > (len(S)):
                break

for i in st_list:
    j = i -1

    if j < 0:
        pass
    else:
        while S[j] == '>':
            ans[j] = max(ans[j+1]+1,ans[j])
            j -= 1
            if j < 0:
                break

print(sum(ans))