contests = [i for i in range(100,1000) if i % 111 == 0]
N = int(input())
for contest in contests:
  if contest >= N:
    print(contest)
    break
  else:
    continue
