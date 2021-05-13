S = list(input())
data=[0]*(len(S)+1)
for i in range(len(S)):
  if S[i] == "<":
    data[i+1] = data[i] + 1
for i in range(len(S)):
  if S[len(S) - i - 1] == ">":
    data[len(S) -i -1] = max(data[len(S)-i]+1, data[len(S)-1-i])
print(sum(data))