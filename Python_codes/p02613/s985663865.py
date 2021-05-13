N = int(input())
a = 0
w = 0
t = 0
r = 0

x = [0]*N
for i in range(N):
  x[i] = input()
  if x[i] == "AC":
    a += 1
  elif x[i] == "WA":
    w += 1
  elif x[i] == "TLE":
    t += 1
  else:
    r += 1

print("AC x " + str(a))
print("WA x " + str(w))
print("TLE x " + str(t))
print("RE x " + str(r))