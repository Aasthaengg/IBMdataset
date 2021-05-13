S = input()
w = int(input())

c = (len(S)+w-1)//w 
t = 0
Ans =""
while t < c:

  Ans =Ans + S[w*t]
  t += 1

print(Ans)