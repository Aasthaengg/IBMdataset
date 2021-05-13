N,L = map(int,input().split())
a = [0]*N
for i in range(N):
  a[i] = L+i
all_apple_pie = sum(a)
apple_pie = [0]*N
def_apple_pie = [0]*N
for i in range(N):
  t = a[i]
  a[i] = 0
  apple_pie[i] = sum(a)
  def_apple_pie[i] = abs(all_apple_pie-apple_pie[i])
  a[i] = t
index = def_apple_pie.index(min(def_apple_pie))
print(apple_pie[index])