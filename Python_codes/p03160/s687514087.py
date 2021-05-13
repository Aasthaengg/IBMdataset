input1 = input()
input2 = input()

N = int(input1)
h = list(map(int,input2.split()))

c = [0,abs(h[1]-h[0])]

for i in range(2,N):
  c.append(min(c[i-1]+abs(h[i]-h[i-1]),c[i-2]+abs(h[i]-h[i-2])))

print(c.pop())