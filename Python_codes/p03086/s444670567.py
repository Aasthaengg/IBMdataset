S = input()
 
S = list(S)
 
ls = len(S)
count = 0
ans = 0
 #一番最後がATGCでなくとも対応可にしておく
for i in range(ls):
      if S[i] == 'A' or S[i] == 'T' or S[i] == 'G' or S[i] == 'C':
          count += 1
          if count >= ans:
              ans = count
      else:
          count = 0
 
print(ans)