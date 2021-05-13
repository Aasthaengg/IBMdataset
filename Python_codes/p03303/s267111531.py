s=input()
n=int(input())
w=[]
i=0
while i < len(s):
  w.append(s[i])
  i += n
print(''.join(w))