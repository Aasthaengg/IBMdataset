N = int(input())
S = [input() for _ in range(N)]

count = 0
no = 0
end_A = 0
start_B = 0
AB = 0

for i in range(N):
  count += S[i].count("AB")
  if S[i][0] == "B" and S[i][-1] == "A":
    AB+=1
  elif S[i][0] == "B":
    start_B+=1
  elif S[i][-1] == "A":
    end_A+=1
  else:
    no+=1
if end_A >= start_B:
  count +=start_B
  start_B = 0
  end_A -= start_B
else:
  count += end_A
  end_A = 0
  start_B-=end_A

count += max(0,AB-1)

if AB >= 1 and (end_A>0 or start_B>0):
  count += 1
print(count)