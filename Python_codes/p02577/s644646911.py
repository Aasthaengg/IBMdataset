N = int(input())
N_str=str(N)
K=(len(str(N)))
S=0
for i in range(K):
  S += int(N_str[i])

if S%9==0:
    print('Yes')
else:
   print("No")  