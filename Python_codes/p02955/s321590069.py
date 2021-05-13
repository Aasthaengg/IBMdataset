inputs = [int(x) for x in input().split()]
n, k = inputs[0], inputs[1]
ls = [int(x) for x in input().split()]
s = sum(ls)

# https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
divisors = []
for i in range(1, int(s ** 0.5) + 1):
  if s % i == 0:
    divisors.append(i)
    if i != s // i:
      divisors.append(s // i)

divisors.sort(reverse=True)
ans = 1
for d in divisors:
  mods = sorted([l % d for l in ls if l % d != 0])
  opcnt = 0
  is_success = False
  # print("{}: {}".format(d, ", ".join([str(m) for m in mods])))
  while True:
    if opcnt > k or len(mods) == 1:
      # print("opcnt: {}".format(opcnt))
      is_success = False
      break

    if len(mods) == 0:
      is_success = True
      ans = d
      # print("ans: {}, opcnt: {}".format(ans, opcnt))
      break

    if mods[0] + mods[-1] < d:
      mods[-1] += mods[0]
      opcnt += mods[0]
      mods.pop(0)
    elif mods[0] + mods[-1] == d:
      opcnt += mods[0]
      mods.pop(0)
      mods.pop(-1)
    else:
      opcnt += (d - mods[-1])
      mods[0] -= (d - mods[-1])
      mods.pop(-1)
    # print("{}: {}".format(d, ", ".join([str(m) for m in mods])))


  if is_success:
    break

print(ans)


