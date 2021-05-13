n = int(input())
s = []
t = []
for i in range(n):
  s_temp,t_temp = input().split()
  s.append(s_temp)
  t.append(int(t_temp))
end = input()
print(sum(t[s.index(end)+1:]))