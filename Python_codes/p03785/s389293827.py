N, C, K = map(int,input().split())
T = [int(input()) for i in range(N)]
T.sort(reverse = True)
counter = 1
i = 0           #### whileの中のカウント（バス乗車数）
A = T.pop()     #####先頭
while T:
  a = T.pop()
  i+=1
  if i>=C or a>A+K:
    i=0
    A=a
    counter += 1
  
print(counter)