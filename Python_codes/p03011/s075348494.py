P, Q, R = map(int, input().split())
time = [P, Q, R]
result = []
for i in range(len(time)):
  for j in range(i+1, len(time)):
    result.append(time[i]+time[j])
print(min(result))