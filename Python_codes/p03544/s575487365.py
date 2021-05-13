N = int(input())

if N == 1:
  print(1)
  exit()

for i in range(N+1):
    if i == 0:
        L_0 = 2
    elif i == 1:
        L_1 = 1
    else:
        L_2 = L_0 + L_1
        L_0 = L_1
        L_1 = L_2
        
print(L_2)