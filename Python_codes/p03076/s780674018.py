A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
N = [A, B, C, D, E]
loss = []
for i in range(5):
  if N[i]%10 == 0:
    loss.append(10)
  else:
    loss.append(N[i]%10)
Wait = (N[loss.index(min(loss))]) 
N.remove(Wait)
for i in range(4):
  if N[i]%10 == 0:
    Wait += N[i]
  else:
    Wait += ((N[i]//10+1)*10)
print(Wait)