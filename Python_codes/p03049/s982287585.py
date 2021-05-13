N=int(input())

answer=0
num_ba=0
num_a=0
num_b=0
for _ in range(N):
  s=input()
  for i in range(1,len(s)):
    if s[i-1]=="A" and s[i]=="B":
      answer+=1
  
  if s[0]=="B" and s[-1]=="A":
    num_ba+=1
  elif s[0]=="B":
    num_b+=1
  elif s[-1]=="A":
    num_a+=1

if num_ba>0:
  answer+=num_ba-1
  if num_b>0:
    answer+=1
    num_b-=1
  if num_a>0:
    answer+=1
    num_a-=1
  
answer+=min(num_a,num_b)
print(answer)