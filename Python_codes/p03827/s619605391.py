N = int(input())
S = input()
ans = [0]
num = 0
for i in range(N):
    if S[i] == 'I':
        num += 1
        ans.append(num)
    else:
        num -= 1
    ans.append(num)    

print(max(ans))