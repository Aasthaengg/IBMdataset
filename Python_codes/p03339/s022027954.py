N = int(input())
S = input()
S_rep = S.replace('W', '1').replace('E', '0') 

lst1 = [int(S_rep[0])]
for s in S_rep[1:]:
    lst1.append(lst1[-1] + int(s))
ans = [N - lst1[-1] + int(S_rep[0]) - 1]
for i in range(1, N):
    ans.append(lst1[i-1] + N - i - 1 - lst1[-1] + lst1[i])

print(min(ans))