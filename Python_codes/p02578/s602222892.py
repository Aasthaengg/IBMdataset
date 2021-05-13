n = int(input())
tall = input().split(" ")

step = 0
for i in range(n-1):
  c = int(tall[i+1]) - int(tall[i])
  if c < 0:
    step -= c
    tall[i+1] = int(tall[i+1]) - c
print(step)