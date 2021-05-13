N, M = map(int, input().split())
ans_num_lis = [0 for i in range(N)]
pre_ans_lis = [0 for i in range(N)]
ans_lis = [0 for i in range(N)]
for i in range(M):
  problem, result = input().split()
  problem_num = int(problem)
  if result == "WA":
    pre_ans_lis[problem_num-1] += 1
  if result == "AC" and not ans_num_lis[problem_num-1]:
    ans_num_lis[problem_num-1] = 1
    ans_lis[problem_num-1] = pre_ans_lis[problem_num-1]

print(sum(ans_num_lis), sum(ans_lis))