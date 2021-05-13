N = int(input())
participants = sorted([ int(v) for v in input().split(" ") ], reverse=True)

# 1 2 4 5 5 5 7 8 9 
# 1 2 5 5 5 8

sum = 0
for i in range(0, N):
  #print(participants)
  #c_max = participants.pop(0)
  #n_max = participants.pop(0)
  #c_min = participants.pop(-1)
  sum += participants[2*i+1]

print(sum)
