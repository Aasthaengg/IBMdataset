N = int(input())

s = ['a']*N
t = ['a']*N

for i in range(N):
  s[i],t[i] = input().split()

finish = input()

index = s.index(finish)

sum = 0
for i in range(index+1,N):
	sum += int(t[i])
print(sum)