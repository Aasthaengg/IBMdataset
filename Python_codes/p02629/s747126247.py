N = int(input())

alp = "abcdefghijklmnopqrstuvwxyz"
answer = ""

while N != 0:
  N -= 1
  index = N % 26
  answer += alp[index]
  N = N // 26
  
print(answer[::-1])
