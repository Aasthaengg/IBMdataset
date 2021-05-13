n = int(input())

n_str = list(str(n))

for i in range(len(n_str)):
  if n_str[i] == "1":
    n_str[i] = "9"
  else:
    n_str[i] = "1"

print(int("".join(n_str)))