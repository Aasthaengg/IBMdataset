num = list(map(int, input().split()))

sound = num[1] // num[0]

if sound > num[2]:
  sound = num[2]

print(sound)