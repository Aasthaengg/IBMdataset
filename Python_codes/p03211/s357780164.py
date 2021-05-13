S=input()
min_val=10**9
for i in range(len(S)-2):
  temp=abs(753-int(S[i:(i+3)]))
  min_val=min(min_val,temp)
print(min_val)
