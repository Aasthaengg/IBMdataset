S = input()
flag = 0
for dig in S[1:]:
    if dig != "9":
        flag = 1
 
ans = int(S[0]) + 9 * (len(S)-1)
 
if flag == 1:
    ans -= 1
 
print(ans)