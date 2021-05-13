S = input()
K = int(input()) - 1
    
rot = 10 ** 30 + 7

for i in range(len(S)):
    if S[i] != "1":
        rot = i
        break
        
if rot > K:  print("1")
else:  print(S[rot])