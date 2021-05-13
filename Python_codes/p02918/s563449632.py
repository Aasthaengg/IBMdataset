N,K=map(int,input().split())
S=input()

ch_list=[]
for i in range(1,N):
  if S[i-1]!=S[i]:
    ch_list.append(i)
#print(ch_list)
len_ch=len(ch_list)

if len_ch>2*K:
  print(N-1-len_ch+2*K)
else:
  print(N-1)