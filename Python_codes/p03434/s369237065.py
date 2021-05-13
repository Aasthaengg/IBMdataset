N = int(input())
Ali = list(map(int,input().split()))

Ali.sort(reverse = True)

AP = BP = 0

for i in range(N):
  if i%2 == 0:
    AP += Ali[i]
  else:
    BP += Ali[i]

print(AP-BP)