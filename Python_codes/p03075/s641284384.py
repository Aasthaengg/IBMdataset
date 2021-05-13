antennas = []
distance = 0
for _ in range(5):
  antennas.append(int(input()))
distance = int(input())
for i in range(len(antennas)):
  for j in range(i+1, len(antennas)):
    if distance < abs(antennas[i] - antennas[j]):
      print(':(')
      exit()
print('Yay!')