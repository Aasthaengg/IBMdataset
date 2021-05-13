S = input()

cnt = 0
b = 0
for i,s in enumerate(S):
  if s == "W":
    cnt+=b
  else:
    b+=1
print(cnt)
