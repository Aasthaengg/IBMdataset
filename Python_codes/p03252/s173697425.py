S = input()
T = input()
length = len(S)
flg = 1
dic = {}
for i in range(length):
    data = S[i]
    if S[i] not in dic:  dic[S[i]] = T[i]
    else:
        if dic[S[i]] != T[i]:  flg = 0

dic = {}
for i in range(length):
    data = T[i]
    if T[i] not in dic:  
        dic[T[i]] = S[i]
    else:
        if dic[T[i]] != S[i]:  flg = 0
                
if flg:  print("Yes")
else:  print("No")