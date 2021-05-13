num = input()
l =[]

for i in range(num):
   l.append(int(raw_input()))

max = l[1] - l[0]
small = l[0]
for i in range(1, num):
   if small > l[i]:
      small = l[i]
   elif max < l[i] - small:
      max = l[i] - small
print max