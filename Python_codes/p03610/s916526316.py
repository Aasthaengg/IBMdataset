S = input()

num = len(S)//2
ans = []

if len(S) % 2!=0:
    num += 1
    for i in range(num):
        nn = 2*i
        ans.append(S[nn])
else:
    for i in range(num):
        nn = 2*i
        ans.append(S[nn])
        
        
print("".join(ans))