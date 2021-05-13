n, t = map(int, input().split())
times = [int(x) for x in input().split()]

result = 0
for i in range(n - 1):
  if times[i] + t > times[i + 1]:
    tmp = times[i+1] + t - (times[i] + t)
    result += tmp
  else:
    result += t

print(result + t)