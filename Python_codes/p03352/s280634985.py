n = int(input())

answer = 1
for i in range(n//2+1):
  for j in range(2,n//2+1):
    check = i**j
    if check <= n:
      if (answer < check):
        answer = i**j
    else :
      break

print(answer)