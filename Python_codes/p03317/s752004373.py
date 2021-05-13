N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
divide_number = K - 1
other_number = N - 1
answer = 0
answer = other_number // divide_number
if other_number % divide_number != 0:
    answer += 1
print(answer)