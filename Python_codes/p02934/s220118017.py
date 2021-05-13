n = int(input())
an = [int(num) for num in input().split()] 

answer = 0.0
for a in an:
  answer += 1.0/a

answer = 1/answer
print(answer)