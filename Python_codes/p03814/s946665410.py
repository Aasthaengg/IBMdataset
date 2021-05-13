S = input()
len = len(S)
start = len
end = 0
for i in range(len):
  if(S[i] == "A"):
    temp_start = i+1
    start = min(start,temp_start)
  if(S[i] == "Z"):
    temp_end = i+1
    end = max(end,temp_end)
print(end-start+1)