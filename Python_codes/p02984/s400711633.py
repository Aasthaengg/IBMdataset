n = int(input())
l = list(map(int,input().split()))
l2 = [2*l[i] for i in range(n)]
su = 0
for i in l2:
  su -= i
  su *= -1
#print(su)

l_answer = []
a = int(su//2)
s = 0
cou = 1
for i in l2:
  s -= i
  s *= -1
  l_answer.append(s+a*(-1)**cou)
  cou += 1
print(*([l_answer[-1]]+l_answer[:-1]))