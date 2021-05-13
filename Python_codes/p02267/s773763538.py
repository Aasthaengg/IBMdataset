a_N = int(input())
a_list = list(map(int, input().split()))
b_N = int(input())
b_list = list(map(int, input().split()))

answer = 0
for i in b_list:
  if i in a_list:
    answer += 1

print(answer)
