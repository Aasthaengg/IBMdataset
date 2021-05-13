x = [list(map(str, input().split())) for i in range(2)]
a = int(x[0][0])
b = int(x[0][1])
s = x[1][0]
l = []
for i in range(a):
  l += s[i]
l[b-1] = l[b-1].lower()
my_result = l[0]
for i in range(1,a):
  my_result += l[i]
print(str(my_result))