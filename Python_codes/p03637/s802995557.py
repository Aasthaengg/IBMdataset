N = int(input())
A = [int(i) for i in input().split()]

d = {
    "4":0,
    "2":0,
    "1":0
}

for i in A:
  if i%4==0:
    d["4"] += 1
  elif i%2==0:
    d["2"] += 1
  else:
    d["1"] += 1

if d["1"] == 0:
  print("Yes")
elif d["1"] <= d["4"]:
  print("Yes")
elif d["1"] + -(-d["2"]//2) - 1 <= d["4"]:
  print("Yes")
else:
  print("No")