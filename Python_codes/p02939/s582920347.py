s = input()
l = []

prev = ""
pres = ""
cnt = 0

for i in s:
  pres += i
  #print(pres,prev)
  if pres!=prev:
    cnt += 1
    prev = pres
    pres = ""
print(cnt)