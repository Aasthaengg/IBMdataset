s = input()
s = list(s)

ans = []

for i in range(len(s)):
  tmp = s[0:len(s)-(i+1)]
  #print(tmp[0:int(len(tmp)/2)],tmp[int(len(tmp)/2):len(tmp)])
  if tmp[0:int(len(tmp)/2)] == tmp[int(len(tmp)/2):len(tmp)] and len(tmp)%2 == 0:
    ans.append(len(tmp))
    
print(max(ans))