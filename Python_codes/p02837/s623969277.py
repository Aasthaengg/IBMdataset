N = int(input())
a = [[] for _ in range(N)]
for i in range(N):
  A_i = int(input())
  for j in range(A_i):
    a[i].append(list(map(int, input().split())))

max_person = 0
for i in range(2**N):
  judge = True
  bin_num = bin(i)
  times = 0
  for j in reversed(bin_num):
    if j == "b":
      break
    if j == "1":
      for k in a[times]:
        if ((i >> k[0]-1) & 1) != k[1]:
          judge = False
    times += 1
  true_person = bin_num.count("1")
  if judge == True:
    max_person = max(max_person, true_person)
print(max_person)