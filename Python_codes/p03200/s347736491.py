S = input()
cnt = 0
placesum = 0
for i in range(len(S)):
  if S[i] == 'W':
    cnt += 1
    placesum += i
ans = placesum - (cnt*(cnt-1)/2)
print(int(ans))