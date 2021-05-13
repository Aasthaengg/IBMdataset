S = input()
ans = "Yes"
if len(S)%2==1:ans = "No"
for i in range(len(S)//2):
    if S[i*2]+S[i*2+1]!="hi":
        ans = "No"
print(ans)