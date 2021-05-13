S = input()
W = int(input())
for i in range(len(S)):
  if i%W == 0:
    print(S[i],end ='')