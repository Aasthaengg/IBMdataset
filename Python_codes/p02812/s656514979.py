N = int(input())
S = input()
thre = "ABC"
res = 0
for i in range(N-2):
  if thre == S[i:i+3]:
    res +=1
print(res)