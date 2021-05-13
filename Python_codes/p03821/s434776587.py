num = (int)(input())
button = []
for i in range(num):
  button.append(list(map(int, input().split(" "))))
count = 0
for i in range(num - 1, -1, -1):
  button[i][0] += count
  tasu = button[i][1] - (button[i][0] % button[i][1]) if button[i][0] % button[i][1] != 0 else 0
  #print(tasu, count)
  count += tasu
print(count)