S = input()
w = int(input())
list_w = []
for i in range(0,len(S),w):
  list_w.append(S[i])
print(''.join(list_w))

