# B - Increment Decrement
N = int(input())
S = input()
x = 0
ans = [0]
for i in range(N):
    x = x+1 if S[i]=='I' else x-1
    ans.append(x)
print(max(ans))