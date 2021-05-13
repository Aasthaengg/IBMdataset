n= int(input())
music = []
time = []
for i in range(n):
  a,b= input().split()
  music.append(a)
  time.append(int(b))
x = input()
x_index = music.index(x)
print(sum(time[x_index+1:]))
