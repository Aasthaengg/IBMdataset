N = int(input())

numbers_of_testimonies =[]
contents_of_testimonies =[]

for n in range(N):
  testimony = []
  x = int(input())
  numbers_of_testimonies.append(x)
  for _ in range(x):
    testimony.append(list(map(int,input().split())))
  contents_of_testimonies.append(testimony)

numbers_of_testimonies.insert(0,"x")
contents_of_testimonies.insert(0,"x")
ans = 0

for i in range(2**N):
  hypothesis = [0 for _ in range(N)]
  
  for j in range(N):
    if (i>>j) & 1:
      hypothesis[j] = 1
  hypothesis.insert(0,9)
  flag = True
  

  for k in range(1,N+1):
    if hypothesis[k] == 1:

      for l in range(numbers_of_testimonies[k]):
        if contents_of_testimonies[k][l][1] != hypothesis[contents_of_testimonies[k][l][0]]:
          flag = False

  if flag == True:
    ans = max(ans,hypothesis.count(1))
print(ans)