N = int(input())
S = input()
Rc = 0
Gc = 0
Bc = 0
for i in range(N):
    if S[i] == 'R':
         Rc +=1
    elif S[i] == 'G':
         Gc+=1
    elif S[i] == 'B':
         Bc+=1
c = Rc*Gc*Bc

for i in range(N-2):
     for j in range(i+1,N-1):
          if S[i] == S[j]:
               continue
          if j + j - i >= N:
               continue
          if S[i] == S[j+j-i]:
               continue
          if S[j] == S[j+j-i]:
               continue
          c -= 1
print(c)
